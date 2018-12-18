from itertools import combinations
from src.binary_matrix_multiplier import multiplyByVector
from operator import itemgetter

def generate_syndromes_coset_leaders_weights(parity_matrix:[[int]]) -> [([int],[int])]:
    syndrome_count = pow(2, len(parity_matrix))
    syndromes_leaders_weights = []
    coset_leader_len = len(parity_matrix[0])
    leader_generator = _generate_coset_leader(coset_leader_len)
    while len(syndromes_leaders_weights) < syndrome_count:
        leader, count_of_1 = next(leader_generator)
        syndrome = multiplyByVector(parity_matrix, leader)
        if syndrome not in map((lambda s: s[0]), syndromes_leaders_weights):
            syndromes_leaders_weights.append((syndrome, count_of_1))
    return syndromes_leaders_weights

def _generate_coset_leader (length: int) -> ([int],int):
    positions = range(length)
    for count_of_1 in range(length + 1):
        for positions_of_1 in combinations(positions, count_of_1):
            yield ([1 if index in positions_of_1 else 0 for index in range(length)], count_of_1)
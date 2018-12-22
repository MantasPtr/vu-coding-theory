from itertools import combinations
from src.binary_matrix_multiplier import multiplyByVector
from operator import itemgetter

def generate_syndromes_coset_leaders_weights(parity_matrix:[[int]]) -> [([int],[int])]:
    syndrome_count = pow(2, len(parity_matrix))
    syndromes_leaders_weights = []
    coset_leader_len = len(parity_matrix[0])
    leader_generator = _init_coset_leader_generator(coset_leader_len)
    while len(syndromes_leaders_weights) < syndrome_count:
        leader, count_of_1 = next(leader_generator)
        syndrome = multiplyByVector(parity_matrix, leader)
        if syndrome not in map((lambda s: s[0]), syndromes_leaders_weights):
            syndromes_leaders_weights.append((syndrome, count_of_1))
    return syndromes_leaders_weights

def _init_coset_leader_generator (length: int) -> ([int],int):
    # all possible places of 1 in the vector
    positions = range(length)
    
    # increase count of "1" starting from 0
    for count_of_1 in range(length + 1):
        # generate all "1" position combination if there must be count_of_1 "1"
        for positions_of_1 in combinations(positions, count_of_1):
            # 1 if its in generate combination else 0
            coset_leader = [1 if index in positions_of_1 else 0 for index in range(length)]
            yield (coset_leader, count_of_1)
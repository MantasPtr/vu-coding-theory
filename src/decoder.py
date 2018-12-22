from src.syndromes import generate_syndromes_coset_leaders_weights
from src.parity_check_matrix import generate as generate_parity_check
from src.message_splitter import split
from src.binary_matrix_multiplier import multiplyByVector 
from src.exceptions import InvalidStateError

from copy import deepcopy
from itertools import chain

class Decoder:
    def __init__(self, gen_matrix):
        self.gen_matrix = gen_matrix
        self.parity_check_matrix = generate_parity_check(gen_matrix)
        self.list_of_syndromes_coset_leaders_weights = generate_syndromes_coset_leaders_weights(self.parity_check_matrix)
        
    def decode(self, message: [int], message_len: int):
        decoded_vectors = [ self._decode_vector(vector) for vector in split(message, len(self.gen_matrix[0]))]
        return list(chain(*decoded_vectors))[0:message_len]

    def _decode_vector(self, vector: [int]):
        t_vector = deepcopy(vector)
        weight = self._calculate_coset_leader_weight(t_vector)
        if weight == 0:
            return t_vector[0:len(self.gen_matrix)]
        else:
            return self._search_for_decode_vector(0, t_vector, weight)

    def _search_for_decode_vector(self, idx, vector, lowest_weight):
        if idx >= len(vector):
            raise InvalidStateError(f"could not decode vector:{vector}")
        
        vector[idx] ^= 1 
        weight = self._calculate_coset_leader_weight(vector)
        if weight == 0:
            return vector[0 : len(self.gen_matrix)]
        if weight < lowest_weight:
            return self._search_for_decode_vector(idx + 1, vector, weight)
        else:
            vector[idx] ^= 1
            return self._search_for_decode_vector(idx + 1, vector, lowest_weight)

    def _calculate_coset_leader_weight(self, vector):
        decoded = multiplyByVector(self.parity_check_matrix,vector)
        weight = self._find_coset_leader_weight_by_syndrome(decoded)
        return weight

    def _find_coset_leader_weight_by_syndrome(self, syndrome):
        for (s, w) in self.list_of_syndromes_coset_leaders_weights:
            if s == syndrome:
                return w
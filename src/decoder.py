from src  import syndromes
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
        # precalculates syndrome_coset_leader_weight_list
        self.list_of_syndromes_coset_leaders_weights = syndromes.generate_syndromes_coset_leaders_weights(self.parity_check_matrix)
        
    def decode(self, message: [int], message_len: int):
        """Decoded vector using step by step algorithm"""
        # splits message into vectors and decodes each vector 
        decoded_vectors = [ self._decode_vector(vector) for vector in split(message, len(self.gen_matrix[0]))]
        # combines decoded vectors into single vector and reduces its length to orginal message length
        return list(chain(*decoded_vectors))[:message_len]

    def _decode_vector(self, vector: [int]):
        """Decoded vector using step by step algorithm - low level actions """
        # make copy of original vector - we don't want to modify it since it may be used elsewhere
        t_vector = deepcopy(vector)
        # get coset leader weight
        weight = self._calculate_coset_leader_weight(t_vector)
        # if coset leader weight is 0 we decoded the vector 
        if weight == 0:
            # since generating matrix is standart - decoded vector is first bits equal to matrix row count
            return t_vector[:len(self.gen_matrix)] 
        else:
            # initiate search for lowest errors
            return self._search_for_decode_vector(0, t_vector, weight)

    def _search_for_decode_vector(self, idx, vector, lowest_weight):
        """Tries to decode vector by fliping 'vector' bit in 'idx' position by checking if got closer """
        # validation that we did not pass all the vector without finding the correct vector
        if idx >= len(vector):
            # this should never happen
            raise InvalidStateError(f"could not decode vector:{vector}")
        # flips bit in idx position
        vector[idx] ^= 1 
        # find coset leader weight
        weight = self._calculate_coset_leader_weight(vector)
        # if coset leader weight is 0 we decoded the vector 
        if weight == 0:
            # since generating matrix is standart - decoded vector is first bits equal to matrix row count
            return vector[:len(self.gen_matrix)]
        if weight < lowest_weight:
            # new weight is lower than previous lovest - keep bit flipped and keep trying other bits 
            return self._search_for_decode_vector(idx + 1, vector, weight)
        else:
            # new weight is same or greater than previous lovest - restore flipped bit and keep trying other bits
            vector[idx] ^= 1
            return self._search_for_decode_vector(idx + 1, vector, lowest_weight)

    def _calculate_coset_leader_weight(self, vector):
        """ decodes vector and finds its coset leader weight """ 
        decoded = multiplyByVector(self.parity_check_matrix, vector)
        
        weight = self._find_coset_leader_weight_by_syndrome(decoded)
        return weight

    def _find_coset_leader_weight_by_syndrome(self, syndrome):
        """finds weight by precalculated syndrome - cosset leader list"""
        for (s, w) in self.list_of_syndromes_coset_leaders_weights:
            if s == syndrome:
                return w
from src.binary_matrix_multiplier import multiplyByMatrix
from src.message_splitter import split, append_0_if_short

from itertools import chain

def encode_message(message: [int], matrix):
        encoded_vectors = [
            encode_vector(append_0_if_short(vector, len(matrix)), matrix) 
            for vector in split(message, len(matrix))
            ]
        return list(chain(*encoded_vectors))

def encode_vector(vector, matrix) -> [int]:
        return multiplyByMatrix(vector, matrix)

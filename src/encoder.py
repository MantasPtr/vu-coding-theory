from src.binary_matrix_multiplier import multiplyByMatrix
from src.message_splitter import split, append_0_if_short

from itertools import chain

def encode_message(message: [int], matrix):
        # splits message into vectors, then appends 0 if its too short, then encodes it
        encoded_vectors = [
            encode_vector(append_0_if_short(vector, len(matrix)), matrix) 
            for vector in split(message, len(matrix))
            ]
        # joins all vectors into one long sequence
        return list(chain(*encoded_vectors))

def encode_vector(vector, matrix) -> [int]:
        """ Encodes vector by generating martrix """
        return multiplyByMatrix(vector, matrix)

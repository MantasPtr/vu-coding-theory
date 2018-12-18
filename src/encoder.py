from src.binary_matrix_multiplier import multiplyByMatrix
from src.exceptions import InvalidArgumentError
from itertools import chain

def encode_message(message: [int], matrix):
        encoded_vectors = [encode_vector(vector, matrix) for vector in _split_into(message, len(matrix))]
        return list(chain(*encoded_vectors))

def encode_vector(vector, matrix) -> [int]:
        return multiplyByMatrix(vector, matrix)

def _split_into(message: [int], length) -> [[int]]:
    if (length < 1):
        raise InvalidArgumentError("cannot split vector into arrays of length less than 1")
    for position in range(0, len(message), length):
        splitted = message[position:position + length]
        yield _append_0_if_short(splitted, length)
        
def _append_0_if_short(vector: [int], length) -> [int]:
    for _ in range(len(vector),length):
        vector.append(0)
    return vector
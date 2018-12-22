import argparse

from src.exceptions import InvalidArgumentError
import src.matrix_generator as matrix_generator

def parse_program_args():
    args = _read_args()
    return parse_args(args)

def parse_args(args):
    k = args.k
    n = args.n
    msgStr = args.msg
    gen_matrix = args.m
    error_chance = args.e
    gen_matrix = _resolve_matrix(gen_matrix, k, n)
    msg = _vector_to_list(msgStr)
    _validate_chance(error_chance)
    return k, n, msg, gen_matrix, error_chance

def _resolve_matrix(gen_matrix, k, n):
    if (gen_matrix is None):
        gen_matrix = matrix_generator.generate(k,n)
    else:
        gen_matrix = _matrix_to_list(gen_matrix)
        if (len(gen_matrix) != k):
            raise InvalidArgumentError(f"Generating matrix dimension does not match k argument. k = {k}, matrix row count = {len(gen_matrix)}") 
        if (len(gen_matrix[0]) != n):
            raise InvalidArgumentError(f"Generating matrix dimension does not match n argument. k = {n}, matrix col count = {len(gen_matrix[0])}") 
    return gen_matrix

def _read_args():
    parser = argparse.ArgumentParser(description='Encodes vector or a file using a binary matrix then decodes using step by step decoding')
    parser.add_argument('k', metavar="k", type=int, help='Code dimension')
    parser.add_argument('n', metavar="n", type=int, help='Code length')
    parser.add_argument('msg', metavar="msg", type=str, help='message to send')
    parser.add_argument('-m', metavar="[[X, X ... , X], [X, X ... , X] ... [X, X, ..., X]]", type=str, default=None, help='Generator matrix')
    parser.add_argument('-e', metavar="0.XXX",  type=float, default=0.1, help='error chance (0-1)')
    return parser.parse_args()

def _validate_chance(error_chance):
     if not (0 <=  error_chance <= 1):
        raise InvalidArgumentError(f"invalid error chance")
   

def _matrix_to_list(matrixStr : str, begin_string="[", end_string="]", separator: str = ","):
    """converts string of vectors to list of vectors."""
    if not (matrixStr.startswith(begin_string) and matrixStr.endswith(end_string)):
        raise InvalidArgumentError(f"matrix {matrixStr} does not starts with {begin_string} or ends with {end_string}")
    begin_idx = len(begin_string)
    end_idx = len(matrixStr) - len(end_string)
    matrixStr = matrixStr[begin_idx:end_idx]
    vectors = matrixStr.split(separator)
    return [_vector_to_list(vector) for vector in vectors]

def _vector_to_list(vector: str):
    """converts vector string to list of binary digits."""
    if not _is_vector_valid(vector):
        raise InvalidArgumentError(f"vector: {vector} contains illegal characters")
    return [ int(letter) for letter in vector ]

def _is_vector_valid(message: str):
    for symbol in message:
        if symbol != '0' and symbol != '1':
            return False
    return True
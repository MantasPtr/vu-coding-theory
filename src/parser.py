from src.exceptions import InvalidArgumentError

def matrix_to_list(matrixStr : str, begin_string="[", end_string="]", separator: str = ",") -> [[int]]:
    """converts string of vectors to list of vectors."""
    if not (matrixStr.startswith(begin_string) and matrixStr.endswith(end_string)):
        raise InvalidArgumentError(f"matrix {matrixStr} does not starts with {begin_string} or ends with {end_string}")
    begin_idx = len(begin_string)
    end_idx = len(matrixStr) - len(end_string)
    matrixStr = matrixStr[begin_idx:end_idx]
    vectors = matrixStr.split(separator)
    return [vector_to_list(vector) for vector in vectors]

def vector_to_list(vector: str) -> [int]:
    """converts vector string to list of binary digits."""
    if not _is_vector_valid(vector):
        raise InvalidArgumentError(f"vector: {vector} contains illegal characters")
    return [ int(letter) for letter in vector ]

def _is_vector_valid(message: str):
    for symbol in message:
        if symbol != '0' and symbol != '1':
            return False
    return True

def list_to_vector(vector: [int]) -> str:
    return ''.join(str(c) for c in vector)

def list_to_matrix(matrix: [[int]]) -> str:
    string_matrix = ",".join([list_to_vector(vector) for vector in matrix])
    return "[" + string_matrix + "]" 
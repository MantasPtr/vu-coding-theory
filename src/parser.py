from src.exceptions import InvalidArgumentError

def vector_to_list(vector: str) -> [int]:
    """converts vector string to list of binary digits."""
    return [ int(letter) for letter in vector ]

def list_to_vector(vector: [int]) -> str:
    """converts list of binary digits to vector string."""
    return ''.join(str(c) for c in vector)

def list_to_matrix(matrix: [[int]]) -> str:
    """converts list of binary digits to matrix string."""
    string_matrix = ",".join([list_to_vector(vector) for vector in matrix])
    return "[" + string_matrix + "]" 
from src.exceptions import InvalidArgumentError

def multiply(vector, matrix):
    if not vector:
        raise InvalidArgumentError("vector must me not empty list")
    if not matrix:
        raise InvalidArgumentError("matrix must me not empty list")
    if len(vector) != len (matrix):
        raise InvalidArgumentError(f"cannot multiply vector which length is {len(vector)} by matrix that has a {len(matrix)} rows")
    if not all(isinstance(row,list) for row in matrix):
        raise InvalidArgumentError(f"not all matrix rows are lists")
    if not all(len(row)==len(matrix[0]) for row in matrix):
        raise InvalidArgumentError(f"not all matrix rows are equal length")
    # for row,idx in enumerate(matrix):
    return []
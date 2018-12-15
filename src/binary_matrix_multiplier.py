from src.exceptions import InvalidArgumentError

def multiply(vector: [int], matrix:[[int]]):
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

    result = [0 for _ in range(len(matrix[0]))] # initialize empty array
    for matrix_column_idx, _  in enumerate(matrix[0]):
        for matrix_row_idx, v_value in enumerate(vector):
            result[matrix_column_idx] ^= (v_value * matrix[matrix_row_idx][matrix_column_idx])
    return result
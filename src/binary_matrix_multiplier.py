from src.exceptions import InvalidArgumentError

def multiplyByMatrix(vector: [int], matrix:[[int]]):
    # vector x matrix
    _validate(matrix, vector)
    if len(vector) != len (matrix):
        raise InvalidArgumentError(f"cannot multiply vector which length is {len(vector)} by matrix that has a {len(matrix)} rows")
    result = [0 for _ in range(len(matrix[0]))] # initialize empty array
    for matrix_column_idx, _  in enumerate(matrix[0]):
        for matrix_row_idx, v_value in enumerate(vector):
            result[matrix_column_idx] ^= (v_value * matrix[matrix_row_idx][matrix_column_idx])
    return result

def multiplyByVector(matrix:[[int]], vector: [int]):
     # matrix x vector
     # assuming vector and result are tramsposed
    _validate(matrix, vector)
    if len(matrix[0]) != len(vector):
         raise InvalidArgumentError(f"cannot multiply vector which length is {len(vector)} by matrix that has a {len(matrix[0])} columns")
    result = [0 for _ in range(len(matrix))] # initialize empty array
    for matrix_row_idx, _ in enumerate(matrix):
        for matrix_column_idx, v_value  in enumerate(vector):
            result[matrix_row_idx] ^= (v_value * matrix[matrix_row_idx][matrix_column_idx])
    return result

def _validate(matrix:[[int]], vector: [int]):
    # vector x matrix
    if not vector:
        raise InvalidArgumentError("vector must me not empty list")
    if not matrix:
        raise InvalidArgumentError("matrix must me not empty list")
    if not all(isinstance(row,list) for row in matrix):
        raise InvalidArgumentError(f"not all matrix rows are lists")
    if not all(len(row)==len(matrix[0]) for row in matrix):
        raise InvalidArgumentError(f"not all matrix rows are equal length")
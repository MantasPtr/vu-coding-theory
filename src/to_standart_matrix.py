# import copy
# import src.exceptions as exc

# def convert(matrix: [[int]]) -> ([[int]],[(int,int)]):
#     matrix_copy = copy.deepcopy(matrix)
#     return _standart_step(matrix_copy)

# def _standart_step(matrix: [[int]], column = 0, row = 0, swaps = []):
#     # if (swaps == None):
#     #     swaps = []
#     if (row >= len(matrix) or column >= len(matrix[0])):
#         return matrix
#     column_has_1, row_with_1_index = _find_first_1_in_column(matrix, row, column)
#     if not column_has_1: # did not find 1 in a column
#         if (column + 1 == len(matrix[0]) and row + 1 == len(matrix)):
#             raise exc.InvalidArgumentError("cannot convert matrix to standart matrix")
#         row_has_1, column_with_1_index   = _find_first_1_in_a_row(matrix[row], column)
#         if row_has_1:
#             matrix = _swap_columns(matrix,column_with_1_index,column)
#             return _standart_step(matrix, column, row)
#         raise NotImplementedError("Not implement swap")
#     else:
#         matrix = _swap_rows(matrix, row, row_with_1_index)
#         matrix = _xor_others_if_not_0(matrix, row, column)
#         return _standart_step(matrix, column+1, row + 1)

# def _find_first_1_in_column(matrix, row_to_start: int, column: int) -> (bool,int):
#     for row_idx in range(row_to_start, len(matrix)):
#         if matrix[row_idx][column] == 1:
#             return True,row_idx
#     return False, -1

# def _find_first_1_in_a_row(row: [int], start_col: int) -> (bool,int):
#     for col_idx in range(start_col, len(row)):
#         if row[col_idx] == 1:
#             return True,col_idx
#     return False, -1

# def _swap_rows(matrix: [[int]], a: int, b: int) -> [[int]]:
#     matrix[a], matrix[b] = matrix[b],matrix[a]
#     return matrix

# def _swap_columns(matrix: [[int]], a: int, b: int) -> [[int]]:
#     for row in matrix:
#         row[a], row[b] = row[b],row[a]
#     return matrix

# def _xor_others_if_not_0(matrix: [[int]], main_row: int, column: int) -> [[int]]:
#     return [
#         [value^matrix[main_row][value_idx] 
#             for value_idx, value in enumerate(row)] 
#         if row_idx != main_row and row[column] == 1 else row 
#         for row_idx, row in enumerate(matrix) ]
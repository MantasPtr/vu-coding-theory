from src.matrix_generator import generate_0_matrix
from src.exceptions import InvalidStateError

def generate(gen_matrix: [[int]]):
    """Creates partity check matrix by generating matrix"""
    k = len(gen_matrix)
    n = len(gen_matrix[0])
    # prefills  matrix with 0
    parity_matrix = generate_0_matrix(row_count = n-k, column_count = n)
    _transpose_end_into_begining(gen_matrix, parity_matrix, k, n )
    _fill_end_with_standart_matrix(parity_matrix, col_from = k, col_to = n)
    if (parity_matrix == []):
        raise InvalidStateError(f"Could not generate parity matrix. Gen matrix = {gen_matrix}")
    return parity_matrix

def _transpose_end_into_begining(gen_matrix, parity_matrix, k, n):
    """ Tranposes the last n-k columns of the generating matrix, and sets them as first beginnings oft the rows of parity martix"""
    for row_idx in range(k):
        for col_idx in range(k, n):
            parity_matrix[col_idx-k][row_idx] = gen_matrix[row_idx][col_idx]

def _fill_end_with_standart_matrix(parity_matrix, col_from, col_to):
    """ Fills last columns of parity matrix with standart matrix"""
    row_counter = 0
    # fills the diagonal with 1s
    for i in range(col_from, col_to):
        parity_matrix[row_counter][i] = 1 
        row_counter += 1


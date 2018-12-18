def generate(gen_matrix: [[int]]):
    k = len(gen_matrix)
    n = len(gen_matrix[0])
    parity_matrix = _generate_0_matrix(row_count = n-k, column_count = n)
    _transpose_end_into_begining(gen_matrix, parity_matrix, k, n )
    _fill_end_with_standart_matrix(parity_matrix, row_from = k, row_to = n)
    
    return parity_matrix


def _generate_0_matrix(row_count, column_count):
    return [[0 for _ in range(column_count)] for _ in range(row_count)]

def _transpose_end_into_begining(gen_matrix, parity_matrix,  k, n):
    for row_idx in range(k):
        for col_idx in range(k, n):
            parity_matrix[col_idx-k][row_idx] = gen_matrix[row_idx][col_idx]

def _fill_end_with_standart_matrix(parity_matrix, row_from, row_to):
    row_counter = 0
    for i in range(row_from,row_to):
        parity_matrix[row_counter][i] = 1 
        row_counter += 1


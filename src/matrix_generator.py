import random

def generate(row_count, col_count):
    """Creates genering matrix"""
    # initiates random
    gen = random.Random()
    # empty matrix
    matrix = generate_0_matrix(row_count, col_count)
    # fills diagonal with 1
    for v in range(row_count):
        matrix[v][v] = 1
    # fills rest of values with 0 or 1
    for row in range(row_count):
        for col in range(row_count, col_count):
            random_chance = gen.random()
            # 50% to replace 0 with 1
            if (random_chance > 0.5):
                matrix[row][col] = 1
    return matrix
    
def generate_0_matrix(row_count, column_count):
    """Generates matrix that is only contains 0"""
    return [[0 for _ in range(column_count)] for _ in range(row_count)]

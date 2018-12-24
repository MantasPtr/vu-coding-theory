import random

def generate(row_count, col_count):
    
    gen = random.Random()
    matrix = generate_0_matrix(row_count, col_count)
    print(row_count, col_count)
    for v in range(row_count):
        matrix[v][v] = 1
    for row in range(row_count):
        for col in range(row_count, col_count):
            random_chance = gen.random()
            if (random_chance > 0.5):
                matrix[row][col] = 1
    return matrix
    
def generate_0_matrix(row_count, column_count):
    return [[0 for _ in range(column_count)] for _ in range(row_count)]

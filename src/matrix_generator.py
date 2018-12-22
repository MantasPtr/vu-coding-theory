import random

def generate(k, n):
    gen = random.Random()
    matrix = generate_0_matrix(k,n)
    for v in range(k):
        matrix[v][v] = 1
    for row in range(k):
        for col in range(k,n):
            random_chance = gen.random()
            if (random_chance > 0.5):
                matrix[row][col] = 1
    return matrix
    
def generate_0_matrix(row_count, column_count):
    return [[0 for _ in range(column_count)] for _ in range(row_count)]

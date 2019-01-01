from src.exceptions import ValidationError
from src import parser

def validate_k_n(k, n):
    # checks if value fields contained a value
    _validate_not_empty(k, "K value must be provided.")
    _validate_not_empty(n, "N value must be provided.")
    # tries to convert values to numbers if values were numbers
    try:
        k = int(k)
    except ValueError:
        raise ValidationError(f"Invalid K value. Cannot convert {k} to number")           
    try:
        n = int(n)
    except ValueError:
        raise ValidationError(f"Invalid N value. Cannot convert {n} to number")
    # k and n must be 1 or greater
    if k < 1:
        raise ValidationError(f"Invalid K value. K must be positive, now its value is  {k}")
    if n < 1:
        raise ValidationError(f"Invalid N value. N must be positive, now its value is  {n}")
    # (k <= n) for standart matrix
    if (n < k):
        raise ValidationError(f"Invalid K - ({k}) and N  - ({n}) values. For standart matrix, is required that k <= n")
    return k, n

def validate_vector(vector: str):
     # checks if value fields contained a value
    _validate_not_empty(vector, "Vector must be provided.")
    # checks if vector contains only binary characters
    if not _vector_consist_of_0_and_1(vector):
        raise ValidationError(f"Invalid vector value - ({vector}). It must only contain values of 0 and 1")
    # converts vector string to list of binary values
    vector = parser.vector_to_list(vector)
    return vector

def _vector_consist_of_0_and_1(message: str):
    """checks if all characters are either 0 or 1"""
    return all( map( (lambda symbol: symbol == '0' or symbol == '1'), message))
    
def validate_error_chance(error_chance: str):
     # checks if value fields contained a value
    _validate_not_empty(error_chance, "Error chance value must be provided. Value must be between 0 and 1")
    # tries convert value to number 
    if (error_chance is not float):
        try:
            error_chance = float(error_chance)
        except ValueError:
            raise ValidationError(f"Invalid error chance value. Cannot convert {error_chance} to number")           
    # checks if value os from interval [0,1]
    if not (0 <=  error_chance <= 1):
            raise ValidationError(f"Invalid error chance value. Value must be between 0 and 1, now its {error_chance}")
    return error_chance

def validate_gen_matrix(matrix: str) -> [[int]]:
    """validates converts generating matrix string to list of vectors."""
    begin_string = "["
    end_string = "]"
    separator = ","
    # check if the matrix string is in correct format
    if not (matrix.startswith(begin_string) and matrix.endswith(end_string)):
        raise ValidationError(f"Invalid matrix value. Matrix {matrix} does not starts with {begin_string} or ends with {end_string}")
    # remove begin and end characters
    begin_idx = len(begin_string)
    end_idx = len(matrix) - len(end_string)
    matrix_str = matrix[begin_idx:end_idx]
    # matrix splits string into vector strings
    vectorsStr = matrix_str.split(separator)
    # validates that matrix contains any vectors
    if (vectorsStr == []):
        raise ValidationError(f"Invalid matrix value. Matrix {matrix} does not contain any vectors")
    # validates that all vectors in matrix is the same length
    if any(map (lambda vector: len(vector) != len(vectorsStr[0]), vectorsStr)):
        raise ValidationError(f"Invalid matrix value. Not all matrix rows are equal length")
    try:
        matrix = [validate_vector(vector) for vector in vectorsStr]
    except ValidationError as ve:
        raise ValidationError(f"Invalid matrix vector. {ve.message}", ve)
    # (k <= n) for standart matrix
    if (len(matrix) >= len(matrix[0])):
        raise ValidationError(f"Invalid matrix vector. It must contains more columns than rows (otherwise parity matrix cannot be generated)")
    # checks if matrix is standart
    validate_that_matrix_is_standart(matrix)
    return matrix

def validate_error_vector(error_vector_str: str, encoded_vector: [int]):
    # checks if value field contained a value
    _validate_not_empty(error_vector_str, f"Invalid error vector value. It must must contain at least one character")
    # checks if error vector contains only binary characters
    if not _vector_consist_of_0_and_1(error_vector_str):
        raise ValidationError(f"Invalid error vector value - ({error_vector_str}). It must only contain values of 0 and 1")
    # converts error vector string to list of digits
    error_vector = parser.vector_to_list(error_vector_str)
    # checks if error vector length is the same as encoded vector length
    if len(error_vector) != len(encoded_vector):
        raise ValidationError(f"Invalid error vector value - ({error_vector_str}). It must be same length as encoded vector")
    return error_vector

def validate_that_matrix_is_standart(matrix: [[int]]):
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if col_idx < len(matrix):
                if col_idx != row_idx:
                    # checks if not diagonal contains only 0 
                    if value != 0:
                        raise ValidationError(f"Invalid matrix. It is not standart matrix." +
                           f"Value at row {row_idx+1}, column {col_idx+1} must be 0.")
                else:
                    # checks if diagonal contains only 1 
                    if value != 1:
                        raise ValidationError(f"Invalid matrix. It is not standart matrix." +
                           f"Value at row {row_idx+1}, column {col_idx+1} must be 1.")

def _validate_not_empty(value: str, message: str):
    if value == "":
        raise ValidationError(message)
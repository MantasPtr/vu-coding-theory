import unittest
from src import validator 
from src.exceptions import ValidationError
class TestValidator(unittest.TestCase):

    # vector encoding
    def test_validation_empty(self):
        self.assertTrue(validator._vector_consist_of_0_and_1(""))
    
    def test_validation_bin(self):
        self.assertTrue(validator._vector_consist_of_0_and_1("10010010"))
     
    def test_validation_not_bin(self):
        self.assertFalse(validator._vector_consist_of_0_and_1("10sadasd01dasdasd0010")) 

    def test_empty_vector(self):
        vector = ""
        self._assert_invalid_vector(vector)

    def test_abc_vector(self):
        vector = "abc"
        self._assert_invalid_vector(vector)

    def test_0_vector(self):
        vector = "0"
        result = [0]
        self._assert_valid_vector(vector, result)

    def test_101_vector(self):
        vector = "101"
        result = [1,0,1]
        self._assert_valid_vector(vector, result)

    def test_empty_matrix_str(self):
        matrix = ""
        self._assert_invalid_matrix(matrix)

    def test_empty_matrix(self):
        matrix = "[]"
        self._assert_invalid_matrix(matrix)

    def test_not_equal_row_matrix(self):
        matrix = "[1,01]"
        self._assert_invalid_matrix(matrix)

    def test_not_binary_row_matrix(self):
        matrix = "[121],[021]]"
        self._assert_invalid_matrix(matrix)
    
    def test_imposible_parity_martix_binary_row_matrix(self):
        matrix = "[10,01,01]"
        self._assert_invalid_matrix(matrix)
    
    def test_valid_matrix_1x3(self):
        matrix = "[111]"
        rez = [[1,1,1]]
        self._assert_valid_matrix(matrix, rez)

    def test_valid_matrix_3x2(self):
        matrix = "[100,011]"
        rez = [[1,0,0],[0,1,1]]
        self._assert_valid_matrix(matrix, rez)

    def test_not_standart_matrix_extra_1(self):
        matrix = "[110,011]"
        self._assert_invalid_matrix(matrix)
    
    def test_not_standart_matrix_extra_0(self):
        matrix = "[100,001]"
        self._assert_invalid_matrix(matrix)

    def _assert_valid_vector(self, vector, result):
        self.assertEqual(result,validator.validate_vector(vector))

    def _assert_invalid_vector(self, vector):
        with self.assertRaises(ValidationError):
            validator.validate_vector(vector)
    
    def _assert_valid_matrix(self, matrix, result):
        self.assertEqual(result,validator.validate_gen_matrix(matrix))
    
    def _assert_invalid_matrix(self, matrix):
        with self.assertRaises(ValidationError):
            validator.validate_gen_matrix(matrix)

if __name__ == '__main__':
    unittest.main()
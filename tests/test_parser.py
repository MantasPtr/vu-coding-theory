import unittest
from src import parser
class TestEncoder(unittest.TestCase):

    # vector encoding
    def test_vector_str_vector_5(self):
        input = [1,1,0,0,1]
        string = parser.list_to_vector(input)
        output = parser.vector_to_list(string)
        self.assertEqual(input, output)

    def test_vector_str_vector_0(self):
        input = []
        string = parser.list_to_vector(input)
        output = parser.vector_to_list(string)
        self.assertEqual(input, output)

    def test_matrix_str_matrix_2x5(self):
        input = [[1,0,1],[1,1,0]]
        string = parser.list_to_matrix(input)
        output = parser.matrix_to_list(string)
        self.assertEqual(input, output)

    def test_validation_empty(self):
        self.assertTrue(parser._is_vector_valid(""))
    
    def test_validation_bin(self):
        self.assertTrue(parser._is_vector_valid("10010010"))
     
    def test_validation_not_bin(self):
        self.assertFalse(parser._is_vector_valid("10sadasd01dasdasd0010"))
     


if __name__ == '__main__':
    unittest.main()
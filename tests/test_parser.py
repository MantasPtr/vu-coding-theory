import unittest
from src import parser

class TestParser(unittest.TestCase):

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
        
if __name__ == '__main__':
    unittest.main()
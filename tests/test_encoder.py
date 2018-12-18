import unittest
from src import encoder

class TestEncoder(unittest.TestCase):

    # vector encoding

    def test_encode_1_1x1(self):
        input = [1]
        gen_matrix = [[1]]
        output = [1]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)

    def test_encode_0_1x1(self):
        input = [0]
        gen_matrix = [[1]]
        output = [0]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)

    def test_encode_11_2x2(self):
        input = [1,1]
        gen_matrix = [[1,0],[1,1]]
        output = [0,1]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)

    def test_encode_10_2x2(self):
        input = [1,0]
        gen_matrix = [[1,0],[1,1]]
        output = [1,0]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)

    def test_encode_vectors_4x3_1(self):
        input = [1,1,0]
        gen_matrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0]]
        output = [1,0,1,1]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)
    
    def test_encode_vectors_4x3_2(self):
        input = [0,1,0]
        gen_matrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0]]
        output = [0,1,1,1]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)
    
    def test_encode_vectors_4x3_3(self):
        input = [0,0,1]
        gen_matrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0]]
        output = [1,0,1,0]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)

    def test_encode_vectors_4x3_4(self):
        input = [1,1,1]
        gen_matrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0]]
        output = [0,0,0,1]
        rez = encoder.encode_vector(input, gen_matrix)
        self.assertEqual(rez, output)
        
    # message encoding


    def test_encode_message_4x3(self):
        input = [1,1,0,0,1,0,0,0,1,1,1,1]
        gen_matrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0]]
        output = [1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1]
        rez = encoder.encode_message(input, gen_matrix)
        self.assertEqual(rez, output)

    def test_encode_message_not_full(self):
        input = [1,1,0,0,1]
        gen_matrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0]]
        output = [1,0,1,1,0,1,1,1]
        rez = encoder.encode_message(input, gen_matrix)
        self.assertEqual(rez, output)
if __name__ == '__main__':
    unittest.main()
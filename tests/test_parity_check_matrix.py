import unittest
from src import parity_check_matrix as pcm

class TestParityMatrixGeneration(unittest.TestCase):

    def test_parity_1x2(self):
        gen_matrix = [[1,0]]
        parity_check_matrix = [[0,1]]
        self.assertEqual(pcm.generate(gen_matrix), parity_check_matrix)

    def test_parity_3x5(self):
        gen_matrix = [[1,0,1,0,1],[0,1,1,1,0]]
        parity_check_matrix = [[1,1,1,0,0],[0,1,0,1,0],[1,0,0,0,1]]
        self.assertEqual(pcm.generate(gen_matrix), parity_check_matrix)

    def test_parity_1x3(self):
        gen_matrix = [[1,1,1]]
        parity_check_matrix = [[1,1,0],[1,0,1]]
        self.assertEqual(pcm.generate(gen_matrix), parity_check_matrix)

    def test_parity_3x6(self):
        gen_matrix = [
            [1,0,0,0,0,1],
            [0,1,0,1,0,1],
            [0,0,1,0,1,0],
        ]
        parity_check_matrix = [
            [0,1,0,1,0,0],
            [0,0,1,0,1,0],
            [1,1,0,0,0,1]]
        self.assertEqual(pcm.generate(gen_matrix), parity_check_matrix)


if __name__ == '__main__':
    unittest.main()
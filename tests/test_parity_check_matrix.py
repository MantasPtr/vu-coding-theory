import unittest
from src import parity_check_matrix as sm

class TestParityMatrixGeneration(unittest.TestCase):
     
    def test_dimensions_12(self):
        rez = sm.generate([[1,0]])
    #     self.assertEqual(len(rez), 2)
    #     self.assertEqual(len(rez[0]), 1)

    # def test_dimensions_32(self):
    #     rez = pcm.generate([[1,0],[1,0],[1,0]])
    #     self.assertEqual(len(rez), 2)
    #     self.assertEqual(len(rez[0]), 3) 

if __name__ == '__main__':
    unittest.main()
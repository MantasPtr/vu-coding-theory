import unittest
from src.binary_matrix_multiplier import multiplyByVector
from src.exceptions import InvalidArgumentError 
class Test(unittest.TestCase):

    def test_000(self):
        self.assertEqual(multiplyByVector([[1,1,0], [1,0,1]] , [0,0,0]), [0,0])

    def test_001(self):
        self.assertEqual(multiplyByVector([[1,1,0], [1,0,1]] , [0,0,1]), [0,1])

    def test_010(self):
        self.assertEqual(multiplyByVector([[1,1,0], [1,0,1]] , [0,1,0]), [1,0])

    def test_100(self):
        self.assertEqual(multiplyByVector([[1,1,0], [1,0,1]] , [1,0,0]), [1,1])

    def test_wrong_length(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByVector([1,1], [[0,1]])

if __name__ == '__main__':
    unittest.main()
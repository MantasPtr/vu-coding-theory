import unittest
from src.binary_matrix_multiplier import multiplyByMatrix
from src.exceptions import InvalidArgumentError 
class TestBitMultiplier(unittest.TestCase):

    def test_101(self):
        self.assertEqual(multiplyByMatrix([1,1,0], [[1,1,0,0], [0,1,1,1], [1,0,1,0]]), [1,0,1,1])

    def test_010(self):
        self.assertEqual(multiplyByMatrix([0,1,0], [[1,1,0,0], [0,1,1,1], [1,0,1,0]]), [0,1,1,1])

    def test_001(self):
        self.assertEqual(multiplyByMatrix([0,0,1], [[1,1,0,0], [0,1,1,1], [1,0,1,0]]), [1,0,1,0])

    def test_compress(self):
        self.assertEqual(multiplyByMatrix([1,0,1], [[1,0], [0,1], [1,1]]), [0,1])

    def test_one(self):
        self.assertEqual(multiplyByMatrix([1,0,1], [[1,0,0], [0,1,0], [0,0,1, ]]), [1,0,1])
     
    def test_wrong_length(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix([1,1], [[0,1]])

    def test_empty_vector(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix([], [[1]])

    def test_empty_matrix(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix([1], [])

    def test_no_vector(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix(None, [[1]])

    def test_no_matrix(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix([1], None)

    def test_not_all_rows_matrix(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix([1,1,1], [[1], None, [1]])

    def test_not_equal_row_length_matrix(self):
        with self.assertRaises(InvalidArgumentError):
            multiplyByMatrix([1,1,1], [[1], [1,1], [1]])
            
if __name__ == '__main__':
    unittest.main()
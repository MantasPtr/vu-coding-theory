import unittest
from src.message_splitter import split as si
from src.exceptions import InvalidArgumentError
class TestSplitInto(unittest.TestCase):

    def test_empty(self):
        input = []
        length = 1
        rez = []
        self.assertEqual(list(si(input,length)),rez)

    def test_len_0(self):
        input = [1]
        length = 0
        rez = []
        with self.assertRaises(InvalidArgumentError):
            self.assertEqual(list(si(input,length)),rez)
    
    def test_parity_4_by_2(self):
        input =  [1,2,3,4]
        length = 2
        rez = [[1,2],[3,4]]
        self.assertEqual(list(si(input,length)),rez)

    def test_parity_5_by_2(self):
        input =  [1,2,3,4,5]
        length = 2
        rez = [[1,2],[3,4],[5]]
        self.assertEqual(list(si(input,length)),rez)

if __name__ == '__main__':
    unittest.main()
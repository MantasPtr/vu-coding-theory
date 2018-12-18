import unittest
from src.syndromes import _generate_coset_leader
class TestGenerateCosetLeader(unittest.TestCase):

    def test_0(self):
        gen = _generate_coset_leader(0)
        self.assertEqual(next(gen), ([],0))

    def test_1(self):
        gen = _generate_coset_leader(1)
        self.assertEqual(next(gen), ([0],0))
        self.assertEqual(next(gen), ([1],1))

    def test_2(self):
        gen = _generate_coset_leader(2)
        self.assertEqual(next(gen), ([0,0],0))
        self.assertEqual(next(gen), ([1,0],1))
        self.assertEqual(next(gen), ([0,1],1))
        self.assertEqual(next(gen), ([1,1],2))

if __name__ == '__main__':
    unittest.main()
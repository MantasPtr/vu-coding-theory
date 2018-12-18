import unittest
from src.syndromes import generate_syndromes_coset_leaders_weights
class Test(unittest.TestCase):

    def test_000(self):
        parity_matrix = [[1,1,0], [1,0,1]]
        syndromes_coset_leaders = generate_syndromes_coset_leaders_weights(parity_matrix) 
        self.assertEqual(syndromes_coset_leaders[0], ([0,0],0))
    
    def test_2x3(self):
        parity_matrix = [[1,1,0], [1,0,1]]
        syndromes_coset_leaders = generate_syndromes_coset_leaders_weights(parity_matrix)
        rez =  [([0,0],0),([0,1],1),([1,0],1),([1,1],1)]
        self.assertTrue(sorted(syndromes_coset_leaders) == sorted(rez))

if __name__ == '__main__':
    unittest.main()
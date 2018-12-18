import unittest
from src.decoder import Decoder

class TestDecoder(unittest.TestCase):

    def test_doc_egz(self):
        gen_matrix = [
            [1,1,0,1,0,0],
            [0,1,1,0,1,0],
            [1,0,1,0,0,1]
        ]
        vector = [1,1,1,0,0,0]
        decoded = [0,1,1,0,1,0]
        
        decoder = Decoder(gen_matrix)
        rez = decoder.decode(vector, len(vector))
        self.assertEqual(decoded, rez)

if __name__ == '__main__':
    unittest.main()
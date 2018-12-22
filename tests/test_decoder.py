import unittest
from src.decoder import Decoder
from src.encoder import encode_vector, encode_message
class TestEncoderDecoder(unittest.TestCase):

    def test_encode_decode(self):
        gen_matrix = [
            [1,0,0,0,0,1],
            [0,1,0,1,0,1],
            [0,0,1,0,1,1],
        ]
        msg = [1,1,1]
        vector = encode_message(msg, gen_matrix)
        decoder = Decoder(gen_matrix)
        rez = decoder.decode(vector, len(vector))
        self.assertEqual(msg, rez)

    def test_encode_decode_1_mistake_len_2(self):
        gen_matrix = [
            [1,0,1,0,0,1],
            [0,1,1,1,0,1],
        ]
        msg = [1,1]
        vector = encode_message(msg, gen_matrix)
        decoder = Decoder(gen_matrix)
        for idx in range(len(vector)):
            vector[idx] ^= 1
            rez = decoder.decode(vector, len(vector))
            self.assertEqual(msg, rez, f"not equal after changing bit in position {idx}")
            vector[idx] ^= 1

# python -m unittest tests.test_decoder.TestEncoderDecoder.test_encode_decode_1_mistake_at_pos_4
    # def test_encode_decode_1_mistake_at_pos_4(self):
    #     gen_matrix = [
    #         [1,0,0,0,0,1],
    #         [0,1,0,1,0,1],
    #         [0,0,1,0,1,0],
    #     ]
    #     msg = [1,1,1]
    #     vector = encode_message(msg, gen_matrix)
    #     decoder = Decoder(gen_matrix)
    #     vector[4] ^= 1
    #     rez = decoder.decode(vector, len(vector))
    #     self.assertEqual(msg, rez, f"not equal after changing bit in position 4")
        
    # def test_encod
    # e_decode_1_mistake(self):
    #     gen_matrix = [
    #         [1,0,0,0,0,1],
    #         [0,1,0,1,0,1],
    #         [0,0,1,0,1,0],
    #     ]
    #     msg = [1,1,1]
    #     vector = encode_message(msg, gen_matrix)
    #     decoder = Decoder(gen_matrix)
    #     for idx in range(len(vector)):
    #         vector[idx] ^= 1
    #         rez = decoder.decode(vector, len(vector))
    #         self.assertEqual(msg, rez, f"not equal after changing bit in position {idx}")
    #         vector[idx] ^= 1

if __name__ == '__main__':
    unittest.main()
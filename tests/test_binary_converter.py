import unittest
from src import binary_converter
class TestBinaryConverter(unittest.TestCase):

    def test_encode_decode_abc(self):
        text = "abc"
        vector = binary_converter.text_to_bits(text)
        rez = binary_converter.bits_to_text(vector)
        self.assertEqual(text, rez)

    def test_encode_decode_ž(self):
        text = "ž"
        vector = binary_converter.text_to_bits(text)
        rez = binary_converter.bits_to_text(vector)
        self.assertEqual(text, rez)

if __name__ == '__main__':
    unittest.main()
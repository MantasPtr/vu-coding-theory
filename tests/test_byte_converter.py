import unittest
from src import byte_converter as bc

class TestByteConverter(unittest.TestCase):

    def test_validation_empty(self):
        self.assertTrue(bc.validate_string(""))
    
    def test_validation_bin(self):
        self.assertTrue(bc.validate_string("10010010"))
     
    def test_validation_not_bin(self):
        self.assertFalse(bc.validate_string("10sadasd01dasdasd0010"))
     
if __name__ == '__main__':
    unittest.main()
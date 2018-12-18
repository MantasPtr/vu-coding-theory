# import unittest
# from src import to_standart_matrix as sm
# from src import exceptions

# class TestConvertToStandartMatrix(unittest.TestCase):

#     def test_to_standart_1x1(self):
#         matrix = [[1]]
#         rez = [[1]]
#         self.assertEqual(sm.convert(matrix),rez)

#     def test_to_standart_1x1_zero(self):
#         matrix = [[0]]
#         with self.assertRaises(exceptions.InvalidArgumentError):
#             sm.convert(matrix)

#     def test_to_standart_2x2_no_action(self):
#         matrix = [[1,0],[0,1]]
#         rez = [[1,0],[0,1]]
#         self.assertEqual(sm.convert(matrix),rez)

#     def test_to_standart_2x2_same(self):
#         matrix = [[1,0],[1,0]]
#         with self.assertRaises(exceptions.InvalidArgumentError):
#             sm.convert(matrix)

#     def test_to_standart_2x2_reversed(self):
#         matrix = [[0,1],[1,0]]
#         rez = [[1,0],[0,1]]
#         self.assertEqual(sm.convert(matrix),rez)

#     def test_to_standart_4x5(self):
#         matrix = [[0,1,0,1],[1,0,1,0],[1,0,1,1],[1,0,0,0],[0,0,0,0]]
#         rez = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
#         self.assertEqual(sm.convert(matrix),rez)

#     def test_to_standart_2x3_with_col_swap(self):
#         matrix = [[1,0,0],[0,0,1]]
#         rez = [[1,0,0],[0,1,0]]
#         self.assertEqual(sm.convert(matrix),rez)

#     def test_to_standart_3x3_no_with_zero_row(self):
#         matrix = [[1,0,0],[0,0,0],[0,0,1]]
#         with self.assertRaises(exceptions.InvalidArgumentError):
#             sm.convert(matrix)
    
#     def test_to_standart_3x3_with_equal_rows(self):
#         matrix = [[1,0,0],[0,0,1],[0,0,1]]
#         with self.assertRaises(exceptions.InvalidArgumentError):
#             sm.convert(matrix)

#     def test_to_standart_3x2_with_row_swap(self):
#         matrix = [[1,0],[0,0],[0,1]]
#         rez = [[1,0],[0,1],[0,0]]
#         self.assertEqual(sm.convert(matrix),rez)

#     def test_row_xor_1x1(self):
#         matrix = [[1]]
#         row = 0
#         column = 0
#         rez = [[1]]
#         self.assertEqual(sm._xor_others_if_not_0(matrix, row, column),rez)

#     def test_row_xor_2x3(self):
#         matrix = [[1,0,1],[1,0,0]]
#         row = 1
#         column = 0
#         rez = [[0,0,1],[1,0,0]]
#         self.assertEqual(sm._xor_others_if_not_0(matrix, row, column),rez)

#     def test_row_xor_start_0(self):
#         matrix = [[1,0],[0,1]]
#         row = 0
#         column = 0
#         rez = [[1,0],[0,1]]
#         self.assertEqual(sm._xor_others_if_not_0(matrix, row, column),rez)
        
#     def test_row_xor_2_col(self):
#         matrix = [[1,1,1],[1,0,1],[0,1,0]]
#         row = 0
#         column = 1
#         rez = [[1,1,1],[1,0,1],[1,0,1]]
#         self.assertEqual(sm._xor_others_if_not_0(matrix, row, column),rez)
    
#     def test_row_xor_4x6(self):
#         matrix = [[1,0,0,1,0,1],[1,0,0,1,0,1],[0,1,1,0,1,0],[1,0,0,0,0,0]]
#         row = 0
#         column = 0
#         rez = [[1,0,0,1,0,1],[0,0,0,0,0,0],[0,1,1,0,1,0],[0,0,0,1,0,1]]
#         self.assertEqual(sm._xor_others_if_not_0(matrix, row, column),rez)

   


# if __name__ == '__main__':
#     unittest.main()
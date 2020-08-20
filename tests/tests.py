import sys
import unittest
sys.path.insert(0, "../mktable2matrix/")
from mktable2matrix import *

class TestMkTable2Matrix(unittest.TestCase):
    def test_split_complete_line(self):
        test_input = '|a|b|c|'
        expected_output = ['','a','b','c','']
        returned_output = parse_line(test_input)
        
        self.assertEqual(returned_output, expected_output)
    
    def test_split_missing_value_line(self):
        test_input = '|a||c|'
        expected_output = ['','a','','c','']
        returned_output = parse_line(test_input)
        
        self.assertEqual(returned_output, expected_output)

    def test_split_missing_all_values_line(self):
        test_input = '||||'
        expected_output = ['','','','','']
        returned_output = parse_line(test_input)
        
        self.assertEqual(returned_output, expected_output)
        
    def test_markdown_to_table_method_with_headers(self):
        test_input = '|a|b|c|d|\n| - | - | - | - |\n|a|b|c|d|\n|a|b|c|d|'
        expected_output = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']]
        returned_output = to_matrix(test_input)
        
        self.assertEqual(returned_output, expected_output)

    def test_markdown_to_table_method_without_headers(self):
        test_input = '|a|b|c|d|\n|a|b|c|d|'
        expected_output = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']]
        returned_output = to_matrix(test_input, has_headers=False)
        
        self.assertEqual(returned_output, expected_output)

if __name__ == '__main__':
    unittest.main()
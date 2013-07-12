"""
       File : test_count_comparisons_last_pivot.py
     Author : Drew Verlee
       Date : 11.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test count comparisons using last pivot
"""

import unittest
from quick_sort_project import quick_sort, file_to_list, last


#take care with the relative paths
class TestCountComparisonslast(unittest.TestCase):
    """count the number of comparisons made during quick sort
    """
    
    def test_file_count_comparisons_from_10txt(self):
        i = file_to_list('../test_files/10.txt')
        expected = 29
        _, returned= quick_sort(i, last)
        self.assertEqual(expected, returned)


    def test_file_count_comparisons_from_100txt(self):
        i = file_to_list('../test_files/100.txt')
        expected = 587
        _, returned= quick_sort(i, last)
        self.assertEqual(expected, returned)

    def test_file_count_comparisons_from_1000txt(self):
        i = file_to_list('../test_files/1000.txt')
        expected = 10184
        _, returned= quick_sort(i, last)
        self.assertEqual(expected, returned)

if __name__ == '__main__':
    unittest.main()

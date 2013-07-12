"""
       File : test_count_comparisons_first_pivot.py
     Author : Drew Verlee
       Date : 11.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : count the comparisons if pivot is always first ele
"""

import unittest
from quick_sort_project import quick_sort, file_to_list, first


#take care with the relative paths
class TestCountComparisonsFirst(unittest.TestCase):
    """count the number of comparisons made during quick sort
    """
    
    def test_file_count_comparisons_from_10txt(self):
        i = file_to_list('../test_files/10.txt')
        expected = 25
        _, returned= quick_sort(i, first)
        self.assertEqual(expected, returned)


    def test_file_count_comparisons_from_100txt(self):
        i = file_to_list('../test_files/100.txt')
        expected = 615
        _, returned= quick_sort(i, first)
        self.assertEqual(expected, returned)

    def test_file_count_comparisons_from_1000txt(self):
        i = file_to_list('../test_files/1000.txt')
        expected = 10297
        _, returned= quick_sort(i, first)
        self.assertEqual(expected, returned)

if __name__ == '__main__':
    unittest.main()

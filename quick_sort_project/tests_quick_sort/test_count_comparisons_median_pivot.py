"""
       File : test_count_comparisons_median_pivot.py
     Author : Drew Verlee
       Date : 11.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tests for pivot if the median
"""

import unittest
from quick_sort_project import quick_sort, file_to_list, median_of_three


#take care with the relative paths
class TestCountComparisonsMeidan(unittest.TestCase):
    """count the number of comparisons made during quick sort
    """

    def test_file_count_comparisons_from_10txt(self):
        i = file_to_list('../test_files/10.txt')
        expected = 21
        _, returned= quick_sort(i, median_of_three)
        self.assertEqual(expected, returned)


    def test_file_count_comparisons_from_100txt(self):
        i = file_to_list('../test_files/100.txt')
        expected = 518
        _, returned= quick_sort(i, median_of_three)
        self.assertEqual(expected, returned)

    def test_file_count_comparisons_from_1000txt(self):
        i = file_to_list('../test_files/1000.txt')
        expected = 8921
        _, returned= quick_sort(i, median_of_three)
        self.assertEqual(expected, returned)

if __name__ == '__main__':
    unittest.main()

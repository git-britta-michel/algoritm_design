"""
       File : test_qsf.py
     Author : Drew Verlee
       Date : 11.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : tests for quick sort with the first ele as the pivot
"""
import unittest
# TODO: see readme

from quick_sort_project import quick_sort
from quick_sort_project import file_to_list


class TestQuickSortSorting(unittest.TestCase):
    """Make sure our quick sort sorts correctly"""

    def test_empty(self):
        i = []
        expected = []
        returned, _ = quick_sort(i)
        self.assertListEqual(expected, returned)


    def test_one_item(self):
        i = [1]
        expected = [1]
        returned, _ = quick_sort(i)
        self.assertListEqual(expected, returned)

    def test_two_items(self):
        i = [2,1]
        expected = [1, 2]
        returned, _ = quick_sort(i)
        self.assertListEqual(expected, returned)

    def test_three_items(self):
        i = [3, 2 ,1]
        expected = [1, 2, 3]
        returned,_ = quick_sort(i)
        self.assertListEqual(expected, returned)

    def test_four_items(self):
        i = [0, 3, 2 ,1]
        expected = [0, 1, 2, 3]
        returned,_ = quick_sort(i)
        self.assertListEqual(expected, returned)

    def test_four_equal(self):
        i = [0, 4, 4 ,4]
        expected = [0, 4, 4, 4]
        returned, _ = quick_sort(i)
        self.assertListEqual(expected, returned)


    def test_file_10txt(self):
        i = file_to_list('../test_files/10.txt')
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result, _ = quick_sort(i)
        self.assertListEqual(expected, result)




if __name__ == '__main__':
    unittest.main()

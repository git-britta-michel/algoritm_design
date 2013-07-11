"""
       File : test_merge_sort.py
     Author : Drew Verlee
       Date : 01.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : testing my merge sort
"""
from merge2 import merge_sort

import unittest

class TestMergeSort(unittest.TestCase):
    """Test case docstring"""


    def test_empty(self):
        i = []
        correct = []
        returned = merge_sort(i)
        self.assertListEqual(correct, returned)


    def test_one_item(self):
        i = [1]
        correct = [1]
        returned = merge_sort(i)
        self.assertListEqual(correct, returned)

    def test_two_items(self):
        i = [2,1]
        correct = [1, 2]
        returned = merge_sort(i)
        self.assertListEqual(correct, returned)

    def test_three_items(self):
        i = [3, 2 ,1]
        correct = [1, 2, 3]
        returned = merge_sort(i)
        self.assertListEqual(correct, returned)

    def test_four_items(self):
        i = [0, 3, 2 ,1]
        correct = [0, 1, 2, 3]
        returned = merge_sort(i)
        self.assertListEqual(correct, returned)

if __name__ == '__main__':
    unittest.main()

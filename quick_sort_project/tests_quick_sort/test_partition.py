"""
       File : test_partition.py
     Author : Drew Verlee
       Date : 11.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : test partition
"""


import unittest
from quick_sort_project import partition
class TestParition(unittest.TestCase):
    """test partitioning around a pivot"""

    def test_empty(self):
        i = []
        expected = []
        returned = partition(i, 0, len(i))
        self.assertListEqual(expected, returned)

    def test_small(self):
        i = [1, 2]
        expected = [], [1], [2]
        returned = partition(i, 0, len(i))
        self.assertTupleEqual(expected, returned)

    def test_small_reversed(self):
        i = [2, 1]
        expected = [1], [2], []
        returned = partition(i, 0, len(i))
        self.assertTupleEqual(expected, returned)

    def test_medium(self):
        i = [5, 4, 10]
        expected = [4], [5], [10]
        returned = partition(i, 0, len(i))
        self.assertTupleEqual(expected, returned)

    def test_large(self):
        i = [5, 4, 10, 6, 12]
        expected = [4], [5], [10, 6, 12]
        returned = partition(i, 0, len(i))
        self.assertTupleEqual(expected, returned)

    def test_extra_large(self):
        i = [5, 2, 5, 8, 10, 3, 4]
        expected = [4, 2, 3], [5], [10, 5, 8]
        returned = partition(i, 0, len(i))
        self.assertTupleEqual(expected, returned)

if __name__ == '__main__':
    unittest.main()

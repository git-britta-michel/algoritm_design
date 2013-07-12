"""
       File : test_median_of_three.py
     Author : Drew Verlee
       Date : 11.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test for median_of_three
"""

import unittest
from quick_sort_project import median_of_three

class TestMedianOfThree(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        i = []
        expected = None
        returned = median_of_three(i)
        self.assertEqual(expected, returned)

    def test_one(self):
        i = [4, 5, 6, 7]
        expected = 1
        returned = median_of_three(i)
        self.assertEqual(expected, returned)

    def test_two(self):
        i = [5, 7, 10, 2, 3]
        expected = 0
        returned = median_of_three(i)
        self.assertEqual(expected, returned)

    def test_three(self):
        i = [10, 12, 2, 1, 20, 4, 8, 3]
        expected = -1
        returned = median_of_three(i)
        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()

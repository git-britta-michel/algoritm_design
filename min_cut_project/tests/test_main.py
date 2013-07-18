"""
       File : test_main.py
     Author : Drew Verlee
       Date : 16.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : TODO add description
"""

import unittest
from min_cut_project.run import main

class TestMain(unittest.TestCase):
    """main tests"""

# TEST ONE OUTLINE
    # 3--4-----5--6
    # |\/|     |\/|
    # |/\|     |/\|
    # 2--1-----7--8

    def test_one(self):
        expected = 2
        result = main('one.txt')
        self.assertEqual(expected, result)

    def test_two(self):
        expected = 2
        result = main('two.txt')
        self.assertEqual(expected, result)

#   TEST THREE OUTLINE
#     3--4-----5--6
#     |\/|     |\/|
#     |/\|     |/\|
#     2--1     7--8

    def test_three(self):
        expected = 1
        result = main('three.txt')
        self.assertEqual(expected, result)

    def test_four(self):
        expected = 1
        result = main('four.txt')
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

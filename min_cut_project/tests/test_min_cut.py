"""
       File : test_min_cut.py
     Author : Drew Verlee
       Date : 16.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : test min cut
"""

import unittest
from min_cut_project.min_cut import min_cut
from min_cut_project.tools import file_to_graph

class TestMinCut(unittest.TestCase):
    """try to find the mind cut"""

    def setUp(self):
        a_file = 'test_data.txt'
        self.G = file_to_graph(a_file)

    def test_small_data(self):
        expected = [2, 3]
        returned = min_cut(self.G)
        self.assertIn(returned, expected)

if __name__ == '__main__':
    unittest.main()

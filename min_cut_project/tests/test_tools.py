"""
       File : test_tools.py
     Author : Drew Verlee
       Date : 16.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tests for min_cut tools
"""

import unittest
from min_cut_project.tools import file_to_graph
class TestFileToGraph(unittest.TestCase):
    """should return a graph"""

    def test_file_simple(self):
        f = 'test_data.txt'
        expected = {
                '1': ['2', '3'],
                '2': ['1', '3', '4'],
                '3': ['1', '2', '4'],
                '4': ['2', '3']
                    }

        returned = file_to_graph(f)
        print returned
        self.assertDictEqual(expected, returned)



if __name__ == '__main__':
    unittest.main()


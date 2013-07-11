"""
       File : test_read_file.py
     Author : Drew Verlee
       Date : 11.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : test are ability to read a file into an array
"""
import unittest
from quick_sort_project import file_to_list

class TestFileToArray(unittest.TestCase):
    """given a file like
    1
    2
    3
    read it into an array => [1,2,3]"""

    def test_with_empty(self):
        a_file = '../test_files/empty.txt'
        result =  file_to_list(a_file)
        expected = []
        self.assertListEqual(result, expected)


    def test_with_file_5txt(self):
        a_file = '../test_files/5.txt'
        result =  file_to_list(a_file)
        expected = [10, 12, 14, 11, 2]
        self.assertListEqual(result, expected)

    def test_with_file_10txt(self):
        a_file = '../test_files/10.txt'
        result =  file_to_list(a_file)
        expected = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

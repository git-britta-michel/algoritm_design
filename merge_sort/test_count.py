"""
       File : test_count.py
     Author : Drew Verlee
       Date : 02.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : TODO add description
"""
from merge2 import merge_sort
from copy import deepcopy as dp
from count_inversions import count_inversions
import unittest

class TestMergeSortCountStr(unittest.TestCase):
    """Test case if merge_sort is given a string"""


    def test_empty(self):
        i = ''
        correct = 0
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)


    def test_no_inversions(self):
        i = '1'
        correct = 0
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_one_inversion(self):
        i = '21'
        correct = 1
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_three_inversions(self):
        i = '321'
        correct = 3
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_larger_three_inversions(self):
        i = '0321'
        correct = 3
        l,inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_four(self):
        i = '135246'
        correct = 3
        l,inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_five(self):
        i = '15324'
        correct = 4
        l,inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_six(self):
        i = '54321'
        correct = 10
        l,inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_seve(self):
        i = '163245'
        correct = 5
        l,inversions = merge_sort(i)
        self.assertEqual(correct, inversions)




    def test_sorted(self):
        i = '1324756890'
        correct = '0123456789'
        j = dp(i)
        l, inversions = merge_sort(j)
        self.assertSequenceEqual(correct, l)

    def more(self):
        a =  [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54] 
        s = ''
        for i in a:
            s += i
        ans = 2372
        l, inversions = merge_sort(s)
        self.assertEqual(ans, inversions)
        



class TestCountInversion(unittest.TestCase):
    """reading a long int from a file"""

    def test_one(self):
        f = 'test_one.txt'
        correct =  22
        inversions = count_inversions(f, merge_sort)
        self.assertEqual(correct, inversions)

# class TestMergeSortCountList(unittest.TestCase):
#     """Test cases if merge_sort is given a list"""


#     def test_empty(self):
#         i = []
#         correct = 0
#         l, inversions = merge_sort(i)
#         self.assertEqual(correct, inversions)


#     def test_no_inversions(self):
#         i = [1]
#         correct = 0
#         l, inversions = merge_sort(i)
#         self.assertEqual(correct, inversions)

#     def test_one_inversion(self):
#         i = [2,1]
#         correct = 1
#         l, inversions = merge_sort(i)
#         self.assertEqual(correct, inversions)

#     def test_three_inversions(self):
#         i = [3, 2 ,1]
#         correct = 3
#         l, inversions = merge_sort(i)
#         self.assertEqual(correct, inversions)

#     def test_larger_three_inversions(self):
#         i = [0, 3, 2 ,1]
#         correct = 3
#         l,inversions = merge_sort(i)
#         self.assertEqual(correct, inversions)

#     def test_sorted(self):
#         correct = [5, 8 ,10, 12, 2, 1]
#         j = dp(correct)
#         l, inversions = merge_sort(j)
#         correct.sort()
#         self.assertListEqual(correct, l)

if __name__ == '__main__':
    unittest.main()

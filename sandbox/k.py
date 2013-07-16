"""
       File : k.py
     Author : Drew Verlee
       Date : 15.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : find the kth largest
"""
import unittest
from random import randrange as rr
from quick_sort_project.my_quick_sort import partition

def kth_largest(A, k):
    """returns the kth element of an array if it were sorted

    :A: list
    :k: int
    :returns: int

        >>> kth_largest([5, 0, 1, 2], 1)
        1
    """
    if A == []: return None
    else:
        l = rr(len(A))
        A[0], A[l] = A[l], A[0]
        less, x, greater = partition(A, 0, len(A))
        if len(less) == k: return x[0]
        elif len(less) < k: return kth_largest(greater, k-(len(less)+len(x)))
        else: return kth_largest(less, k)


class TestK(unittest.TestCase):
    """tests for kth largest"""


    def test_empy(self):
        A = []
        k = 3
        expected  = None
        result = kth_largest(A, k)
        self.assertEqual(expected, result)

    def test_zero(self):
        A = [0, 1, 2]
        k = 0
        expected  = 0
        result = kth_largest(A, k)
        self.assertEqual(expected, result)

    def test_first(self):
        A = [0, 1, 2]
        k = 1
        expected  = 1
        result = kth_largest(A, k)
        self.assertEqual(expected, result)

    def test_small(self):
        A = [5, 0, 2, 1]
        k = 1
        expected  = 1
        result = kth_largest(A, k)
        self.assertEqual(expected, result)

    def test_medium(self):
        A = [8, 0, 1, 5, 2, 4]
        k = 2
        expected  = 2
        result = kth_largest(A, k)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    unittest.main()

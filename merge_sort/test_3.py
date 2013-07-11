import unittest
from merge3 import merge_sort
from copy import deepcopy as dp

class TestMergeSortCountList(unittest.TestCase):
    """Test cases if merge_sort is given a list"""


    def test_empty(self):
        i = []
        correct = 0
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)


    def test_no_inversions(self):
        i = [1]
        correct = 0
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_one_inversion(self):
        i = [2,1]
        correct = 1
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_three_inversions(self):
        i = [3, 2 ,1]
        correct = 3
        l, inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_larger_three_inversions(self):
        i = [0, 3, 2 ,1]
        correct = 3
        l,inversions = merge_sort(i)
        self.assertEqual(correct, inversions)

    def test_sorted(self):
        correct = [5, 8 ,10, 12, 2, 1]
        j = dp(correct)
        l, inversions = merge_sort(j)
        correct.sort()
        self.assertListEqual(correct, l)

if __name__ == '__main__':
    unittest.main()

"""
       File : qs.py
     Author : Drew Verlee
       Date : 10.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : quick_sort
"""
import unittest


def quick_sort(A, pivot_pos=0):
    """sorts an array, if no pivot_position supplied chooses the first

    :A: type, list.
    :returns: a sorted list

    """

    if A == []: return [], 0
    A[0],A[pivot_pos] = A[pivot_pos], A[0]
    pivot = A[0]
    swaps = 0
    l, pivot, g = partition(A, 0, len(A))
    lesser, lswaps = quick_sort(l, pivot_pos)
    greater, gswaps = quick_sort(g, pivot_pos)
    swaps = lswaps + gswaps + len(lesser) + len(greater)
    return lesser + pivot + greater, swaps

def partition(A, l, r):
    """returned a partition list
    :A: a list,
    :l: pivot position
    :r: len of the list
    :returns: a partitioned list according the specifications from
    slide 8 of QuickSort: The partition Subroutine
    """
    if A == []: return []
    p = A[l]
    i = l + 1
    j = l + 1
    while j < r:
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
        j +=1

    A[l], A[i-1] = A[i-1], A[l]
    return A[:i-1], [A[i-1]], A[i:]




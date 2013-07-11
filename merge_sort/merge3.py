"""
       File : merge2.py
     Author : Drew Verlee
       Date : 01.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : another better merge
"""

def merge(left, right):
    """merge the left and right

    :left: sequence
    :right: sequence
    :returns: l+r sorted 

    """
    r,l = 0,0
    left, lc = left
    right, rc = right
    c = lc + rc
    f = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            f.append(left[l])
            l += 1
        else:
            f.append(right[r])
            c += len(left[l:])
            r += 1

    f += left[l:]
    f += right[r:]
    return f, c




def merge_sort(A):
    """@todo: Docstring for merge_sort

    :A: sequence
    :returns: sorted sequence

    """
    l = len(A)
    if l <= 1:
        return A, 0
    else:
        m = l/2
        left = merge_sort(A[:m])
        right = merge_sort(A[m:])
        return merge(left, right)

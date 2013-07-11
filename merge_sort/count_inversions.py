"""
       File : count_inversions.py
     Author : Drew Verlee
       Date : 02.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : for couning inversions in a file
"""

from merge3 import merge_sort
def count_inversions(f, merge_sort):
    L = []
    with open(f, 'r') as long_integer:
        for seg in long_integer:
            L.append(int(seg.strip()))
    _, inversions = merge_sort(L)
    return inversions

if __name__ == '__main__':
    f = 'IntegerArray.txt'
    print count_inversions(f, merge_sort)


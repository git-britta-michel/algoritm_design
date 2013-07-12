"""
       File : tools.py
     Author : Drew Verlee
       Date : 11.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tools for quicksort
"""


def file_to_list(a_file):
    """gives a file read it into an list

    :a_file: filetype, 'AFile.txt', containing 1\n2\n3\n, etc...
    :returns: a list, [1, 2, 3]

    """
    a_list = []
    # this method ensures the file is closed and type changes in one pass
    with open(a_file) as a_file:
        for number in a_file.read().split('\n'):
            if number:
                a_list.append(int(number))
    return a_list

def median_of_three(A):
    """=
    :A: a list
    :returns: the position of the median of the 
    first, middle len(n)/2 -1, last elements of A

    """
    if A == []: return None # not sure this will actual happen
    if (len(A) % 2 == 1): # odd
        middle = len(A)/2
    else: # even
        middle = len(A)/2 -1
    choices = [(A[0], 0), (A[middle], middle), (A[-1], -1)]
    choices.sort()
    return choices[1][1]


def first(): return 0

def last(): return -1

"""
       File : merge_sort.py
     Author : Drew Verlee
       Date : 01.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : a simple merge sort!
"""


def merge_sort(l):
    """@todo: Docstring for merge_sort

    :l: a list!
    :returns: a sorted list!

    """
    # if its of size 1 we just return it
    if len(l) <= 1:
        return l
    if its of size 2 we sort it and return it
    elif len(l) == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        else:
            return l
    else:
    # Now we need to break it into two halfs
        m = len(l)/2
        fhalf, shalf = merge_sort(l[:m]), merge_sort(l[m:])
        j = i = 0
        fl = len(fhalf)
        sl = len(shalf)
        final = []
        while i < sl:
            if fhalf[i] < shalf[j]:
                final.append(fhalf[i])
                i +=1
            else:
                final.append(shalf[j])
                j +=1
            if not j < sl:
                final.extend(fhalf[i:])
                break
        return final


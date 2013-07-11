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
    # reverse tree
    # seg = open(f).read().splitlines()
    # q = deque()
    long_int = []
    with open(f, 'r') as long_integer:
        for seg in long_integer:
            for i in seg.strip():
                long_int.append(int(i))
    _, inversions = merge_sort(long_int)
    return inversions



    # while q:
    #     f, f_inv = merge_sort(q.popleft())
    #     s, s_inv = merge_sort(q.popleft()) 
    #     q.append(f 





    # run merge on the first bottem row collect larger arrays
    # then run again

    # total_inversions = 0
    # L = ''
    # with open(f, 'r') as long_integer:
    #     for seg in long_integer:
    #         merge_sort(seg.strip())
    #         L, i = merge_sort(L)
    #         total_inversions += i
    # sol = open('solution.txt', 'w')
    # sol.write('inversions {0}\nlines {1}'.format(str(total_inversions)))
    # sol.close()
    # return total_inversions



if __name__ == '__main__':
    f = 'IntegerArray.txt'
    print count_inversions(f, merge_sort)


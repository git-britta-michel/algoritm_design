"""
       File : run.py
     Author : Drew Verlee
       Date : 16.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : putting it all together
"""

from tools import lowest, file_to_graph
from min_cut import min_cut
from copy import deepcopy

def main(afile):
    """ takes afile argument"""
    G = file_to_graph(afile)
    return min([min_cut(deepcopy(G)) for x in range(100)])


if __name__ == '__main__':
    print(main('kargerMinCut.txt'))

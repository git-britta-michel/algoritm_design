"""
       File : tools.py
     Author : Drew Verlee
       Date : 16.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : contains the tools for min cut
"""


def file_to_graph(a_file):
    """indented for a sparse matrix

    :a_file: file object, with first column is vertex, rest are columns
    :returns: dict: Graph: {vertex/int: set([neighbor/int, etc..

    """
    # G = {}
    # with open(a_file, 'r') as f:
    #     for line in f:
    #         if line:
    #             line = line.split()
    #             G[line[0]] = line[1:]
    G = {x.split()[0]:x.split()[1:] for x in open(a_file)}
    return G


from copy import deepcopy
def lowest(f, G, p):
    """finds the most lowest return value for a random function

    :f: fucntion with int return
    :G: a graph
    :p: how many times to run the function
    :returns: lowest returned value

    """
    N = deepcopy(G)
    lowest = None
    for x in xrange(p):
        r = f(N)
        if lowest == None:
            lowest = r
        elif r < lowest:
            lowest = r
        if lowest == 2:
            print N
    return lowest

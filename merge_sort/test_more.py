import random
from merge3 import merge_sort as sort_count_inversions

def generate_test_cases(n,m):
    """ Generates and return an random array of n lists each of size m"""
    test_cases=[]
    for i in range(n):
        test_case=[]
        for j in range(m):
            test_case.append(random.randint(1,n))
        test_cases.append(test_case)
    return test_cases

def brute_force_inversions(a):
    """ Brute force algorithm to count number of inversions in a list a"""
    no_of_inversions=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                no_of_inversions+=1
    return no_of_inversions

def test_algorithms(n,m):
    """ Tests the correctness of the devised algorithm for n test cases each of length m"""
    l=generate_test_cases(n,m)
    failed_test_cases=[]
    flag=True
    for item in l:
        count_brute_force_inversions = brute_force_inversions(item)
        temp,count_algorithm_inversions=sort_count_inversions(item)
        if count_brute_force_inversions != count_algorithm_inversions:
            flag=False
            failed_test_cases.append(item)
    if flag:
        print("All Test Cases Passed")
    else:
        print("Some Test Cases Failed")
        print("List of failed test cases are: ")
        print(failed_test_cases)

if __name__ == '__main__':
    test_algorithms(10, 10)

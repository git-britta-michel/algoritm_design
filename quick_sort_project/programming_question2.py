"""
       File : programming_question2.py
     Author : Drew Verlee
       Date : 11.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tests and output generator for programming question two
"""

from quick_sort_project import quick_sort, file_to_list, median_of_three,\
    first, last


import unittest


class TestProgrammingQuestion2(unittest.TestCase):
    """Test cases for programming question 2"""

    my_file = open('solution.txt', 'w')
    my_file.write('Solutions to programming question 2\n')
    my_file.close()

    def setUp(self):
        self.orginal_list = file_to_list('test_files/QuickSort.txt')
        self.solution = open('solution.txt', 'a')

    def tearDown(self):
        self.solution.close()


    def test_question_one(self):
        """question one: if the first pivot is always the first one"""
        q1_list, q1_comparisons = quick_sort(self.orginal_list, first)
        self.orginal_list.sort()
        self.assertListEqual(self.orginal_list, q1_list)
        self.solution.writelines('Question one: {0}\n'.format(q1_comparisons))


    def test_question_two(self):
        """question two: if pivot is alaywas the last element"""
        q2_list, q2_comparisons = quick_sort(self.orginal_list, last)
        self.orginal_list.sort()
        self.assertListEqual(self.orginal_list, q2_list)
        self.solution.write('Question two: {0}\n'.format(q2_comparisons))

    def test_question_three(self):
        """using the 'median-of-three' pivot rule"""
        q3_list, q3_comparisons = quick_sort(self.orginal_list,
                median_of_three)
        self.orginal_list.sort()
        self.assertListEqual(self.orginal_list, q3_list)
        self.solution.write('Question three: {0}\n'.format(q3_comparisons))







if __name__ == '__main__':
    unittest.main()

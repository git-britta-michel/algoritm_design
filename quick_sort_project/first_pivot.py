from quick_sort_project import quick_sort
from quick_sort_project import file_to_list


sorted_list, comparisions = quick_sort(file_to_list('test_files/QuickSort.txt'),0)
print(comparisions)

# import lesson_utils
from lesson_utils import print_matrix as my_print_matrix
import sys
import pprint


matrix = [[0]*5 for i in range(3)]
print_matrix = True
if print_matrix:
    my_print_matrix(matrix)

pprint.pprint(sys.path)


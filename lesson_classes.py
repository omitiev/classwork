# import lesson_utils
from lesson_utils import print_matrix as my_print_matrix
import sys
import pprint

#
# matrix = [[0]*5 for i in range(3)]
# print_matrix = True
# if print_matrix:
#     my_print_matrix(matrix)
#
# pprint.pprint(sys.path)
#

from student import Student
from person import Person

if __name__ == "__main__":
    student1 = Student('Bill', 22)
    print(type(student1))
    student2 = Student('Alice', 24)
    print(type(student2))
    print(id(student1), id(student2))
    student3 = Student('Scot')
    #
    #
    # student1.name = "Bill"
    # student1.age = 22
    # student2.name = "Alice"
    # student2.age = 24
    print(student1.name, student1.age)
    print(student2.name, student2.age)
    print(student3.name, student3.age)

    student1.accepted_task(3, 5, 7, 11, 13, 17, 19)
    student2.accepted_task(1, 2, 3, 4, 5, 6)
    student3.accepted_task(1, 2, 3)

    student1.accepted_test(1, 5, 7, 11, 8, 4, 12)
    student2.accepted_test(1, 2, 3, 4, 5, 6)
    student3.accepted_test(1, 2, 3)



    student1.print_info()
    student2.print_info()
    student3.print_info()

    # pprint.pprint(Student.__dict__)
    # pprint.pprint(student1.__dict__)
    student1.__dict__['name'] = 'William'
    print(student1.__dict__['name'])
    print(student1.name)
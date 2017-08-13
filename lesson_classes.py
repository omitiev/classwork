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


class Student:

    # def __init__(self):
    #     print('Self', self, id(self))
    #     self.name = 'Bill'
    #     self.age = 22
    NUMBER_OF_TASKS = 37
    NUMBER_OF_TESTS = 12
    TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]

    def __init__(self, name, age=18):
        print('Self', self, id(self))
        self.name = name
        self.age = age
        self.hw_results = [0]*Student.NUMBER_OF_TASKS
        self.test_results = [0]*Student.NUMBER_OF_TESTS

    def print_info(self):
        print('_______________________')
        print('Name:', self.name)
        print('Age:', self.age)
        print('H/w results:', self.hw_results)
        print('Test results:', self.test_results)
        print('_______________________')

    def accepted_task(self, *number_of_tasks):
        for task_number in number_of_tasks:
            self.hw_results[task_number-1] = 1

    def accepted_test(self, *number_of_tests):
        for test_number in number_of_tests:
            self.test_results[test_number-1] = 1

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

student1.accepted_task(3, 5, 7, 11, 13, 17, 19)
student2.accepted_task(1, 2, 3, 4, 5, 6)
student3.accepted_task(1, 2, 3)



student1.print_info()
student2.print_info()
student3.print_info()



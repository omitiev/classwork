import random
import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix[0]))
print(type(matrix[0][0]), matrix[0][0])
print(type(matrix[0][1]), matrix[0][1])

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t')
        print()


print_matrix(matrix)

def multiply_matrix_by_n(matrix, n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= n
            # print(matrix[i][j], end='\t')
        print()


multiply_matrix_by_n(matrix, 10)
print_matrix(matrix)

print('-------------')

N = 3
M = 5

# row = [0] * N
# matrix = [row] * M

# for in range(m):               !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     matrix.append(row[:])      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# or  matrix.append(row.copy())
matrix = [[0] * N] * M
print_matrix(matrix)

def initialize_matrix(matrix, lower_bound, upper_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            num = random.randint(lower_bound, upper_bound)
            print(num, end="\t")
            matrix[i][j] = num
        print()

initialize_matrix(matrix, 10, 100)
print("~~~~~~~~~")
print_matrix(matrix)

matrix2 = copy.deepcopy(matrix)
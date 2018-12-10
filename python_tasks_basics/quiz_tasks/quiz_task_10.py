# 10. Вывести на экран матрицу, транспонированную заданной (3*8)

import default
import random


default.start(10)


def create_random_matrix(lower_bound, upper_bound, rows, columns):
    matrix = [[random.randint(lower_bound,upper_bound) for j in range(rows)]for i in range(columns)]
    return matrix


def transpose_matrix(b_matrix):
    t_matrix = [[b_matrix[j][i] for j in range(len(b_matrix))] for i in range(len(b_matrix[0]))]
    return t_matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t')
        print()


mtrx_rows = int(input("Print enter a number of rows for matrix: "))
mtrx_columns = int(input("Print enter a number of columns for matrix: "))
min_value = int(input("Print enter min value for matrix: "))
max_value = int(input("Print enter max value for matrix: "))
base_matrix = create_random_matrix(min_value, max_value, mtrx_rows, mtrx_columns)
print_matrix(base_matrix)
print_matrix(transpose_matrix(base_matrix))


default.end()

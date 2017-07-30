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
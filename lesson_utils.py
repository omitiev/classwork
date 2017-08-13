def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end='\t')
        print()


# var2 = 42
#     print(__name__)

if __name__ == "__name__":
    print_matrix([[1, 2, 3]])
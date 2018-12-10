# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


import default


default.start(6)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 'test', [2]]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'rest', 'test', [1], [1, 2], [2]]


def list_of_equal(lst1, lst2):
    lst3 = []
    for i in lst1:
        for j in lst2:
            if (j == i) and (j not in lst3):
                lst3.append(j)
    return lst3


print("The list of equal items is: ", (list_of_equal(a, b)))


default.end()

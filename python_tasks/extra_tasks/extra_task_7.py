# Write a Python program to remove duplicates from a list.


import default


default.start(7)


def remove_duplicates(base_lst):
    for i in base_lst:
        while base_lst.count(i) > 1:
            base_lst.remove(i)
    return base_lst


usr_lst = list(input("Please enter your list: "))
print("The list without duplicates is: ", (remove_duplicates(usr_lst)))


default.end()

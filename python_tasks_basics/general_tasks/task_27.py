# Создайте список на 50 элементов из всех нечётных чисел от 1 до 99,
# выведите его на экран в строку, а затем этот же список выведите на экран тоже в строку,
# но в случайном порядке (например, 99 11 43 19 … 7 91 3 1).



import default
import random


default.start(27)


def create_list_with_odd(upper_bound):
    odd_lst = []
    for i in range(upper_bound):
        if default.is_odd(i):
            odd_lst.append(str(i))
    return odd_lst


edge = int(input("Please enter a number for upper bound in the list"))
print("Your list is: %s" % (" ".join(create_list_with_odd(edge))))
print("My random list is: %s" % (" ".join(default.random_list(create_list_with_odd(edge)))))


default.end()

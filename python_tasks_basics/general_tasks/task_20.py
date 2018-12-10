# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел списка.
# Т.е. от суммы четных чисел вычесть сумму нечетных чисел в списке.

import default
import random


default.start(20)


def diff_btw_the_sums_of_even_and_odd(min_v, max_v, amount):
    total_even = 0
    total_odd = 0
    for i in range(amount):
        num = random.randint(min_v, max_v)
        if default.is_even(num):
            total_even += num
        else:
            total_odd += num
    print("""
        The sum of even numbers in a range is %i
        The sum of odd numbers in a range is %i""" % (total_even, total_odd))
    diff = total_even - total_odd
    return  diff

min_value = int(input("Please enter min value for the range:"))
max_value = int(input("Please enter max value for the range:"))
amount = int(input("Please enter amount of selection:"))
if min_value > max_value or amount <= 0:
    print("Something went wrong - check the entered data")
else:
    print("The difference between the sums of even and odd is: ", diff_btw_the_sums_of_even_and_odd(min_value, max_value, amount))


default.end()
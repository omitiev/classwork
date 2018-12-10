# Написать функцию для поиска среднего арифметического среди 100 случайно сгенерированных чисел.

import default
import random

default.start(19)


def average_of_random(min_v, max_v, amount):
    total = 0
    for i in range(amount):
        num = random.randint(min_v, max_v)
        total += num
    return total/amount

min_value = int(input("Please enter min value for the range:"))
max_value = int(input("Please enter max value for the range:"))
amount = int(input("Please enter amount of selection:"))
if min_value > max_value or amount <= 0:
    print("Something went wrong - check the entered data")
else:
    print("The average is: ", average_of_random(min_value, max_value, amount))

default.end()
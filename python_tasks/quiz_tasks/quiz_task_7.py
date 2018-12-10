# 7. Найти сумму десяти первых чисел ряда Фибоначчи.

import default


default.start(7)


def fibonacci_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

amount = int(input("Please enter amount of numbers Fibonacci: "))
print("The sum of your sequence Fibonacci is ", (fibonacci_number(amount+1)-1))


default.end()

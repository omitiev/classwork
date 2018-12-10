# 5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.


import default


default.start(5)


def who_closer(x_num, num1, num2):
    if abs(x_num - num1) < abs(x_num - num2):
        return num1
    elif abs(x_num - num1) > abs(x_num - num2):
        return num2


x_num = float(input("Please enter the main number: "))
num1 = float(input("Please enter first number for comparison: "))
num2 = float(input("Please enter second number for comparison: "))
if abs(num1) != abs(num2):
    print("The closer is: ", who_closer(x_num, num1, num2))
else:
    print("The distance for both numbers is equal")

default.end()

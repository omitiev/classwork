# Создать функцию, выводящую на экран случайно сгенерированное 12 ти-значное натуральное число и возвращающую его наибольшую цифру.


import default
import random


default.start(23)


def max_d_in_num(x):
    d_lst = []
    for i in str(x):
        d_lst.append(i)
    return max(d_lst)


a = random.randint(100000000000, 999999999999)
print("Your random number is %i, the biggest digit in number is %s" % (a, max_d_in_num(a)))


default.end()

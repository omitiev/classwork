# Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно.
# Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.

import default

default.start(18)


def total_sum(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    print(total)


int_1 = ord(input("Please enter any symbol:"))
int_2 = ord(input("Please enter any other symbol:"))
if int_1 <= int_2:
    total_sum(int_1, int_2)
else:
    total_sum(int_2, int_1)

default.end()
# Вывести сумму всех чисел, которые являются степенью 3ки и принадлежат диапазону чисел от 0 до 1000000.
# Т.е. sum = 3^0 + 3^1 + 3^2 + ...

import default


default.start(22)


def sum_of_powers(z, upper_bound):
    x = 0
    # z = 3
    i = 0
    while x <= upper_bound:
        x += z**i
        i += 1
    return x


num = int(input("Please enter a digit (e.g. 3): "))
bound = int(input("Please enter an upper bound for range (e.g. 1000000): "))
print(sum_of_powers(num, bound))


default.end()
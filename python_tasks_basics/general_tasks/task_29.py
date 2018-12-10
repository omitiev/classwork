# Создайте список из 11 случайных целых чисел из отрезка [-1;1], выведите список на экран в строку.
# Определите какой элемент встречается в списке чаще всего и выведите об этом сообщение на экран.
# Если два каких-то элемента встречаются одинаковое количество раз, то не выводить ничего.


import default
import random


default.start(29)


lst1 = []
[lst1.append(random.randint(-1, 1)) for i in range(11)]
print("The strange string: %s" % (", ".join([str(i) for i in lst1])))
if (lst1.count(-1) > lst1.count(0)) and (lst1.count(-1) > lst1.count(1)):
    print("The most popular number in the list is -1")
elif (lst1.count(0) > lst1.count(-1)) and (lst1.count(0) > lst1.count(1)):
    print("The most popular number in the list is 0")
elif (lst1.count(1) > lst1.count(-1)) and (lst1.count(1) > lst1.count(0)):
    print("The most popular number in the list is 0")
else:
    print()


default.end()

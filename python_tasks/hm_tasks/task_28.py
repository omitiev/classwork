# Создайте 2 списка из 5 случайных целых чисел из отрезка [0;5] каждый,  выведите списки на экран в двух отдельных строках.
# Посчитайте среднее арифметическое элементов каждого списка и сообщите, для какого из списков это значение оказалось больше
# (либо сообщите, что их средние арифметические равны).


import default
import random


default.start(28)


lst1 = []
lst2 = []
[lst1.append(random.randint(0, 5)) for i in range(5)]
[lst2.append(random.randint(0, 5)) for i in range(5)]
print("First string: %s" % (", ".join([str(i) for i in lst1])))
print("Second string: %s" % (", ".join([str(i) for i in lst2])))
avg_lst1 = sum(lst1) / int(len(lst1))
avg_lst2 = sum(lst2) / int(len(lst2))

if avg_lst1 > avg_lst2:
    print("The average of numbers in the first list is bigger")
elif avg_lst1 < avg_lst2:
    print("The average of numbers in the second list is bigger")
else:
    print("The averages of numbers in the first and second lists are equal")


default.end()

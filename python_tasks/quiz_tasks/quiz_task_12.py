# 12. Для проверки остаточных знаний учеников после летних каникул, учитель младших классов решил начинать каждый урок с того,
# чтобы задавать каждому ученику пример из таблицы умножения, но в классе 15 человек, а примеры среди них не должны повторяться.
# В помощь учителю напишите программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения
# (от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты).
# При этом среди 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)


import default
import random


default.start(12)


def create_list_with_tasks(amount=15):
    lst1 = []
    lst2 = []
    [lst1.append(i) for i in range(2, 10)]
    while len(lst2) < amount:
        num1 = random.choice(lst1)
        num2 = random.choice(lst1)
        x1 = ('%d * %d' % (num1, num2))
        x2 = ('%d * %d' % (num2, num1))
        if (x1 not in lst2) and (x2 not in lst2):
            lst2.append(x1)
    return lst2


print("Today we will decide next tasks: ", create_list_with_tasks())

default.end()

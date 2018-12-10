# Вывести все числа от 0 до 1000, которые содержат в себе цифры 1 и 7. Т.е. числа: 17, 71, 107, 117, 127, 137, …


import default


default.start(21)

for i in range(10001):
    a = '1'
    b = '7'
    num = str(i)
    if (a in num) and (b in num):
        print(num)


default.end()

# Два поезда движутся на скорости V1 и V2 навстречу друг другу.
# Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
# При заданных скоростях узнать столкнутся ли поезда.

import default

default.start(16)
s_1 = 4
s_2 = 6
v_1 = float(input("Please enter velocity of train 1: "))
v_2 = float(input("Please enter velocity of train 2: "))
if v_1 == 0 and v_2 == 0:
    print("The trains don't move")
elif v_2 <= 0 < v_1:
    print("The trains won't crash")
elif v_1 <= 0 < v_2:
    print("The trains will crash")
else:
    print("let's find out will the trains crash in case if the will move towards each other with velocities %.2f km/h and %.2f km/h" % (v_1, v_2))
    t_1 = s_1 / v_1
    t_2 = s_2 / v_2
    if t_1 < t_2:
        print("The trains won't crash")
    else:
        print("The trains will crash")

default.end()
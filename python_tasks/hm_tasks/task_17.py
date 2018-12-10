# Написать функцию решения квадратного уравнения.
# ax**2 + bx + c = 0
# d = b**2 - 4ac
# d > 0 -> x1 and x2; d = 0 -> x1 (x2=x1); d < 0 -> None
# x1 = (-b + sqrt(d)) / 2a ; x2 = (-b - sqrt(d)) / 2a
# var1 = 1 / -70 / 600
# var2 = 3 / -18 / 27
# var3 = 1 / 15 / 100
import math
import default

default.start(17)

def desc(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("""
        x1 = %.2f
        x2 = %.2f""" %(x1, x2))
    elif d == 0:
        x1 = -b / (2*a)
        x2 = x1
        print("""
        x1 = %.2f
        x2 = %.2f""" % (x1, x2))
    else:
        print("None")

print("Let's enter coefficients of quadratic equation ax**2 + bx + c = 0")
a = float(input("Please enter coefficient a:"))
b = float(input("Please enter coefficient b:"))
c = float(input("Please enter coefficient c:"))
if a == 0:
    print("Seems like your equation is linear, and should be decided in other program")
else:
    desc(a, b, c)


default.end()
# (a + b * c)**2     a - 4 * b / c     (a * b + 4) / (c - 1)


import default


default.start(1)


a = float(input("Please, enter a namber for variable a: "))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b: "))
print ("variable b is:", b)
c = float(input("Please, enter a namber for variable c: "))
print ("variable c is:", c)


x1 = (a + b * c)**2
print ("Result of expression (a + b * c)**2 is:", x1)
try:
    x2 = a - 4 * b / c
    print("Result of expression a - 4 * b / c is:", x2)
except ZeroDivisionError:
    print("The expression couldn't be decided because of 'c' variable (ZeroDevisionError)")
try:
    x3 = (a * b + 4) / (c - 1)
    print("Result of expression (a * b + 4) / (c - 1) is:", x3)
except ZeroDivisionError:
    print("The expression couldn't be decided because of 'c' variable (ZeroDevisionError)")


default.end()

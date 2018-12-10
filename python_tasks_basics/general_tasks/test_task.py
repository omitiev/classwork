import math

'''
print ("==========================================================")
print ("test task")
print ("==========================================================")

a=10
b=2

if b!=0:
    c=a/b
    print ("Result of a/b (a=%d, b=%d) is %.2f" % (a, b, c))       - how this row works? please explain on the lesson
else:
    print ("Error: Division by zero")
'''


print ("==========================================================")
print ("task 1")
print ("==========================================================")

a = float(input("Please, enter a namber for variable a"))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b"))
print ("variable b is:", b)
c = float(input("Please, enter a namber for variable c"))
print ("variable c is:", c)
x = a + b * (c / 2)
print ("Result of expression a+b*(c/2) is:" , x)



print ("==========================================================")
print ("task 2")
print ("==========================================================")

a = float(input("Please, enter a namber for variable a"))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b"))
print ("variable b is:", b)
x = (a ** 2 + b ** 2) % 2
print ("Result of expression (a**2+b**2)%2 is:" , x)



print ("==========================================================")
print ("task 3")
print ("==========================================================")

a = float(input("Please, enter a namber for variable a"))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b"))
print ("variable b is:", b)
c = float(input("Please, enter a namber for variable c"))
print ("variable c is:", c)
x = (a + b) / 12 * c % 4 + b
print ("Result of expression (a+b)/12*c%4+b is:" , x)



print ("==========================================================")
print ("task 4")
print ("==========================================================")

a = float(input("Please, enter a namber for variable a"))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b"))
print ("variable b is:", b)
c = float(input("Please, enter a namber for variable c"))
print ("variable c is:", c)
if c!=0:
    x = (a - b * c) / (a + b) % c
    print ("Result of expression (a-b*c)/(a+b)%c is:" , x)
else:
    print ("Error: Sorry operation couldn't be performed due to 'Division by zero' rule")



print ("==========================================================")
print ("task 5")
print ("==========================================================")

a = float(input("Please, enter a namber for variable a"))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b"))
print ("variable b is:", b)
if a+b != 0:
    c = float(input("Please, enter a namber for variable c"))
    print ("variable c is:", c)
    x = math.fabs(a-b) / (a + b) ** 3 - math.cos(c)
    print ("Result of expression |a-b|/(a+b)**3-cos(c) is:" , x)
else:
    print ("Error: Sorry operation couldn't be performed due to 'Division by zero' rule")



print ("==========================================================")
print ("task 6")
print ("==========================================================")

a = float(input("Please, enter a namber for variable a"))
print ("variable a is:", a)
b = float(input("Please, enter a namber for variable b"))
print ("variable b is:", b)
if b != 0:
    c = float(input("Please, enter a namber for variable c"))
    print ("variable c is:", c)
    if c < 0:
        print ("Error: The operation couldn't be performed - variable c should be >= 0")
    else:
        x = (math.log1p(c) / -b)**4 + math.fabs(a)
        print ("Result of expression (ln(1+c)/-b)**4+|a| is:" , x)
else:
    print ("Error: Sorry operation couldn't be performed due to 'Division by zero' rule")
import math
#-----------------------------------------------

def pow(a, b):
    print("I'm inside pow function!")
    return a**b

result = pow(2, 3)
print(result)

#-----------------------------------------------
def rectangle_square (h, w):
    result = h*w
    return result

result2 = rectangle_square(10, 20)
print(result2)

#-----------------------------------------------
def square_square (side):
    result = side*side
    return result

result3 = square_square(20)
print(result3)

#-----------------------------------------------
def square_square (side):
    result = rectangle_square(side, side)
    return result

result4 = square_square(15)
print(result4)

#-----------------------------------------------
def pretty_print (value):
    print("-----------------------------------")
    print("Value:", value)
    print("-----------------------------------")

result2 = rectangle_square(10, 20)
pretty_print(result2)
result4 = square_square(15)
pretty_print(result4)

#-----------------------------------------------
def print_delim():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#-----------------------------------------------
def pretty_print (value):
    print_delim()
    print("Value:", value)
    print_delim()

result2 = rectangle_square(10, 20)
pretty_print(result2)
result4 = square_square(15)
pretty_print(result4)
#-----------------------------------------------

def circle_square (r):
    result = (math.pi * (r**2))
    return result

result5 = circle_square(20)
pretty_print(result5)

#-----------------------------------------------

def add_and_multiply (x, y):
    result1 = x+y
    result2 = x*y
    return result1, result2

result6 = add_and_multiply(2, 3)
pretty_print(result6)
result7, result8 = add_and_multiply(3, 4)
print(result7, result8)

# дефолтное значение для функции ! дефолтные параметры должны идти всегда после недефолтных

def add_and_multiply (x, y=10): # дефолтное значение для функции
    result1 = x+y
    result2 = x*y
    return result1, result2

result6 = add_and_multiply(2) # второе значение не указано - отрабатывается дефолтое значение
pretty_print(result6)

# empty function

# def foo():
#     pass #пасс это заглушка чтобы функция работала - замена ретурну


#*9/5+32

# def cel2far(x):
#     x = x * 9 / 5 + 32
#     return x
#
# a = 36.6
# b = cel2far(a)
# print(b)

def celc2fareng(celc):
    return celc*9/5 + 32

result9 = celc2fareng(36.6)
pretty_print(result9)
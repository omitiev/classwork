import math

#-----------------------------------------
# calculate rect square
height=10
width=20
rectangle_square=height*width
print("rectangle square with height", height, "and width", width, "is -", rectangle_square)
print("rectangle square with height %d and width %d is - %d" % (height, width, rectangle_square))

#-----------------------------------------
# calculate circle square
radius=5
circle_square=(math.pi * (radius**2))
print("circle square:", round(circle_square, 2))
print("circle square with radius %d is - %.2f" % (radius, circle_square))

#-----------------------------------------
# calculate hypotenuse
catheter_a=8
catheter_b=4
hypotenuse= math.sqrt((catheter_a**2)+(catheter_b**2))
print('hypotenuse =', round (hypotenuse, 2))
print("hypotenuse for traingle with catheter_a %.3f and catheter_b %.3f is - %.3f" % (catheter_a, catheter_b, hypotenuse))


s = '\u26bd'
print("symbol %s has unicode -  %d" % (s , ord(s)))

code=0x26BD
print("unicode of %d has symbol - %s" % (code , chr(code)))


#       01234567
time = "18:44:42"
hours = float(time[:2])
print(hours)
minutes = float(time[3:5])
print(minutes)
seconds = float(time[6:])
print(seconds)
total_seconds=hours*3600 + minutes*60 + seconds
print(total_seconds)

lst=time.split(":")
print(lst)

#--------------------------------------------
# unrial variant :)
# #       01234567
# time = "18:44:42"
# idx_colon1 = time.find(":")
# hours = (time[:2])
# print(hours)
# idx_colon2 = time.find(":", idx_colon1)
# minutes = (time[3:5])
# print(minutes)
# idx_colon3 = time.find(":", idx_colon2)
# seconds = (time[6:])
# print(seconds)
# total_seconds=hours*3600 + minutes*60 + seconds
# print(total_seconds)
#
# lst=time.split(":")
# print(lst)

#-----------------------------------------------

#       01234567
time = "20:14:00"
time_lst = time.split(":")
hours = int(time_lst[0])
print(hours)
minutes = int(time_lst[1])
print(minutes)
seconds = int(time_lst[2])
print(seconds)
total_seconds=hours*3600 + minutes*60 + seconds
print(total_seconds)

#-----------------------------------------------

name = "jeff bezos"
name_lst = name.split()
print(name_lst)
name_lst [0] = name_lst[0].capitalize()
name_lst [1] = name_lst[1].capitalize()
print(name_lst)
new_name = name_lst[0] + " " + name_lst[1]
print(new_name)

print(name.title())

#-----------------------------------------------
import re

s = "a,b c:d"
lst = re.split("[, :]", s)
print(lst)



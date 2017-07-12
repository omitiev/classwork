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


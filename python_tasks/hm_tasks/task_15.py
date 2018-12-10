# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.
# r = sqrt( sqr(Xa-Xb) + sqr(Ya-Yb) );

import math
import default

default.start(15)

def is_crossing(radius_1, radius_2, distance):
    if (radius_1 + radius_2) <= distance:
        return False # print("The circles with corresponding coordinates and radiuses don't cross")
    elif ((radius_1 > radius_2) and radius_1 > radius_2 +distance) or ((radius_2 > radius_1) and radius_2 > radius_1 +distance):
        return False # print("The circles with corresponding coordinates and radiuses don't cross (one circle inside the other)")
    else:
        return True # print("The circles with corresponding coordinates and radiuses cross")

circle_coordinates_1 = str(input("Please enter coordinates of center 1-st circle and radius (e.g. 2, 9, 9): "))
circle_coordinates_1_lst = circle_coordinates_1.split(',')
circle_1_x = int(circle_coordinates_1_lst[0])
circle_1_y = int(circle_coordinates_1_lst[1])
radius_1 = int(circle_coordinates_1_lst[2])
circle_coordinates_2 = str(input("Please enter coordinates of center 2-nd circle and radius (e.g. 6, 7, 3): "))
circle_coordinates_2_lst = circle_coordinates_2.split(',')
circle_2_x = int(circle_coordinates_2_lst[0])
circle_2_y = int(circle_coordinates_2_lst[1])
radius_2 = int(circle_coordinates_2_lst[2])
dist_btw_circles = math.sqrt((circle_1_x - circle_2_x)**2 + (circle_1_y - circle_2_y)**2)

if is_crossing(radius_1, radius_2, dist_btw_circles):
    print("The circles with corresponding coordinates and radiuses cross")
else:
    print("The circles with corresponding coordinates and radiuses don't cross")


default.end()
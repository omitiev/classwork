from dot import Dot
import math

class Circle(Dot):
    def __init__(self, coordinate_x, coordinate_y, radius):
        super().__init__(coordinate_x, coordinate_y)
        self.radius = radius


    def print_info_ext(self):
        print("Circle radius: ", self.radius)


    def is_dot_in_circle(self, dot_x, dot_y):
        dist_btw_dots = math.sqrt((dot_x - self.coordinate_x) ** 2 + (dot_y - self.coordinate_y) ** 2)
        return self.radius >= dist_btw_dots

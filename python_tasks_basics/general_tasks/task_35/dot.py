# 35. Создать два класса: Окружность и Точка.
# Создать в классе окружности метод, который принимает в качестве параметра точку и проверяет находится ли данная точка внутри окружности.


class Dot:
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def print_info_ext(self):
        pass

    def print_info(self):
        print('~' * 50)
        print('Coordinate x: ', self.coordinate_x)
        print('Coordinate y: ', self.coordinate_y)
        self.print_info_ext()
        print('~' * 50)

    def get_coordinates(self):
        return self.coordinate_x, self.coordinate_y
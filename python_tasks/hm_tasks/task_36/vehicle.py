# 36. Создать класс Транспортное средство и его потомков - классы Поезд и Самолет.
# В родительском классе должно быть определено минимум 1 инициализатор, 3 атрибута и 1 метод.
# В классах-потомках должны быть добавлены минимум по 1 новому методу и по 1 новому атрибуту.


class Vehicle:
    def __init__(self, type, capacity_of_passengers, direction):
        self.type = type
        self.capacity_of_passengers = capacity_of_passengers
        self.direction = direction

    def print_info_ext(self):
        pass

    def print_info(self):
        print('~'*50)
        print('The type of Vehicle: ', self.type)
        print('Capacity of passengers: ', self.capacity_of_passengers)
        print('The vehicle is able to move to the next direction: ', self.direction)
        self.print_info_ext()
        print('~' * 50)

    def get_direction(self):
        if str.lower(self.direction) == 'free':
            return True
        else:
            return False

    def get_vehicle(self):
        ts = [self.type, int(self.capacity_of_passengers), self.get_direction()]
        return ts

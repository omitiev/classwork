import default
from vehicle import Vehicle
from train import Train
from plain import Plain


default.start(36)


if __name__ == "__main__":
    car = Vehicle('privat', 5, 'free')
    car.print_info()
    print(car.get_vehicle())

    train = Train('public', 340, 'West-North', 'electricity')
    train.print_info()
    print(train.get_train())

    plain = Plain('military', 16, 'FREE', 'react fuel', 130)
    plain.print_info()
    print(plain.get_plain())

default.end()

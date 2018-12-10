from vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, type, capacity_of_passengers, direction, type_of_fuel):
        super().__init__(type, capacity_of_passengers, direction)
        self.type_of_fuel = type_of_fuel

    def print_info_ext(self):
        print("Type of fuel: ", self.type_of_fuel)

    def get_train(self):
        train = self.get_vehicle() + [self.type_of_fuel]
        return train

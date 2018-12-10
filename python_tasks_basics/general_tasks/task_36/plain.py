from vehicle import Vehicle


class Plain(Vehicle):
    def __init__(self, type, capacity_of_passengers, direction, type_of_fuel, min_dist_take_off):
        super().__init__(type, capacity_of_passengers, direction)
        self.type_of_fuel = type_of_fuel
        self.min_dist_take_off = min_dist_take_off

    def print_info_ext(self):
        print("Type of fuel: ", self.type_of_fuel)
        print("The min distance for taking-off is: %d meters" % (self.min_dist_take_off))

    def get_plain(self):
        plain = self.get_vehicle() + [self.type_of_fuel, self.min_dist_take_off]
        return plain

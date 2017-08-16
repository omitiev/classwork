from person import Person

class Professor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    #     self.name = name
    #     self.age = age
        print('_______________________')
    #
    # def print_info(self):
    #     print('_______________________')
    #     print('Name:', self.name)
    #     print('Age:', self.age)
    #     print('_______________________')
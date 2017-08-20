class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info_ext(self):
        pass


    def print_info(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print('Name:', self.name)
        print('Age:', self.age)
        self.print_info_ext()
        print('_______________________')
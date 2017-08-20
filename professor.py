from person import Person

class Professor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    #     self.name = name
    #     self.age = age
        self.salary = 0
        self.groups = []
        self.awards = []
        print('_______________________')

    def print_info(self):
        super().print_info()
        print('Salary:', self.salary)
        if len(self.groups) > 0:
            print('Groups:', self.groups)
        if len(self.awards) > 0:
            print('Scientific award:', self.awards)
        print('_______________________')

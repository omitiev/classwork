from person import Person

class Professor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    #     self.name = name
    #     self.age = age
        self._salary = 0
        self._groups = []
        self.awards = []


    # def print_info(self):
    #     super().print_info()
    #     print('Salary:', self.salary)
    #     if len(self.groups) > 0:
    #         print('Groups:', self.groups)
    #     if len(self.awards) > 0:
    #         print('Scientific award:', self.awards)


    def print_info_ext(self):
        print('Salary:', self._salary)
        if len(self.groups) > 0:
            print('Groups:', self._groups)
        if len(self.awards) > 0:
            print('Scientific award:', self.awards)


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary can't be negative!")
        self._salary = salary

    @property
    def groups(self):
        return self._groups

    def add_group(self, group):
        if len(self._groups) == 3:
            raise ValueError("Too much assigments!")
        self._groups.append(group)

    def remove_group(self, group):
        if group in self._groups:
            self._groups.remove(group)

    def get_group(self):
        return self._groups


    #
    # @groups.setter
    # def groups(self, groups):
    #     if len(groups) > 3:
    #         raise ValueError("Too much assigments!")
    #     self._groups = groups

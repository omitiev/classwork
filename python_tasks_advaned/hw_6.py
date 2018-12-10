"""
Необходимо реализовать метод interact для класса Person, чтобы объекты класса Person научились взаимодействовать
с другими объектами этого класса. Взаимодействие осуществляется путем передачи объекта этого же класса в
качестве аргумента метода interact. Каждый экземпляр класса Person запоминает с кем он взаимодействовал раннее, и
сохраняет запись об этом в атрибут memory Чем "старше" объект класса Person тем меньше пользователей он "помнит"
age <= 25 - помнит всех с кем взаимодействовал
25 < age < 50 - пять последних
50 < age < 75 - двух последних
75 < age < 100 - никого не помнит:)
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.memory = []

    def check_age(self):
        error_msg = "{} is too old"
        if 75 < self.age <= 100:
            return 0
        elif 50 < self.age <= 75:
            return 2
        elif 25 < self.age <= 50:
            return 5
        elif self.age <= 25:
            return float('infinity')
        raise ValueError(error_msg.format(self.name))

    def interact(self, obj):
        self.memory.append({'name': obj.name, 'age': obj.age, 'related_obj': obj})
        if len(self.memory) > self.check_age():
            self.memory.remove(self.memory[0])


bob = Person('bob', 19)
alice = Person('Alice', 25)

bob.interact(alice)
print(bob.memory)  # [{'name': 'Alice', 'age': 25, 'related_obj': <__main__.Person object at 0x054F2550>}]
print(alice.memory)  # []

alice.interact(bob)
print(alice.memory)  # [{'name': 'bob', 'age': 19, 'related_obj': <__main__.Person object at 0x030F2550>}]

steve = Person('Steve', 19)
bob.interact(steve)
print(bob.memory)
# [{'name': 'Alice', 'age': 25, 'related_obj': <__main__.Person object at 0x05AE25F0>},
# {'name': 'Steve', 'age': 19, 'related_obj': <__main__.Person object at 0x05AE2690>}]```

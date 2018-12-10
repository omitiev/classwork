# class MyDict(dict):
#     def __getattr__(self, key):
#         return self[key]
#     def __setattr__(self, key, value):
#         self[key] = value
#
#
# class MyList(list):
#     def append(self, value):
#         return self.append(value)
#
#
#
# class Descr:
#     def __get__ (self, instance, owner):
#         print(instance, owner)
#
#
# class A:
#     attr = Descr()
#
# a = A()
#
# print(a.__dict__)
#
# a.__dict__['attr'] = 1
# print(a.attr)

######################################################################

#
# class MemoryField:
#     def __init__(self):
#         self.memory = []
#
#     def __get__(self, instance, owner):
#         error_msg = "{} is too old"
#         if 75 < instance.age <= 100:
#             return self.memory[0]
#         elif 50 < instance.age <= 75:
#             return self.memory[2]
#         elif 25 < instance.age <= 50:
#             return instance.memory[5]
#         elif instance.age <= 25:
#             return self.memory
#         raise ValueError(error_msg.format(instance.name))
#
#     def __set__(self, instance, value):
#         instance.memory.append({'name': value.name, 'age': value.age, 'related_obj': value})
#
#
# class Person:
#     memory = MemoryField()
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def interact(self, obj):
#         self.memory = obj
#
#
# bob = Person('bob', 19)
# alice = Person('Alice', 25)
#
# bob.interact(alice)
# print(bob.memory)  # [{'name': 'Alice', 'age': 25, 'related_obj': <__main__.Person object at 0x054F2550>}]
# print(alice.memory)  # []
#
# alice.interact(bob)
# print(alice.memory)  # [{'name': 'bob', 'age': 19, 'related_obj': <__main__.Person object at 0x030F2550>}]
#
# steve = Person('Steve', 19)
# bob.interact(steve)
# print(bob.memory)
# # [{'name': 'Alice', 'age': 25, 'related_obj': <__main__.Person object at 0x05AE25F0>},
# # {'name': 'Steve', 'age': 19, 'related_obj': <__main__.Person object at 0x05AE2690>}]```



##################################################################


class MemoryField:
    def __get__(self, instance, owner):
        self.check_key(instance)
        return self.get_result(instance)

    def __set__(self, instance, value):
        self.check_key(instance)
        instance.__dict__[self.name].append({"name": value.name,
                                             "age": value.age,
                                             "related_obj": value})

    def __set_name__(self, owner, name):
        self.name = name

    def check_key(self, instance):
        if not instance.__dict__.get(self.name):
            instance.__dict__[self.name] = []

    def get_result(self, instance):
        """
        age <= 25 - помнит всех с кем взаимодействовал
        25 < age < 50 - пять последних
        50 < age < 75 - двух последних
        75 < age < 100 - никого не помнит
        """
        logic_map = {
            "all": (0, 25),
            5: (25, 50),
            2: (50, 75),
            None: (75, float("inf")),
        }
        for k, v in logic_map.items():
            if v[0] < instance.age <= v[1]:
                if isinstance(k, int):
                    return instance.__dict__[self.name][:k]
                if isinstance(k, str):
                    return instance.__dict__[self.name]
                else:
                    return []

class Person:
    memory = MemoryField()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def interact(self, obj):
        self.memory = obj


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
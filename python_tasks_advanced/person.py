'''
Усовершенствовать класс Person, создать дескриптор OnlyASCII, благодаря которому в качестве имени можно будет использовать только ASCII символы.
class OnlyASCII:

Усовершенствовать класс Person, создать дескриптор IntegerField, благодаря которому в качестве возраста можно будет использовать только числа типа int
'''


class OnlyASCII:
   def __get__(self, instance, owner):
       return instance.__dict__[self.name]

   def __set__(self, instance, value):
       if value.isascii():
           instance.__dict__[self.name] = value
           return instance.__dict__[self.name]
       raise ValueError('Name is not in ASCII')

   def __set_name__(self, owner, name):
       self.name = name


class IntegerField:
   def __get__(self, instance, owner):
       return instance.__dict__[self.name]

   def __set__(self, instance, value):
       if isinstance(value, int):
           instance.__dict__[self.name] = value
           return instance.__dict__[self.name]
       raise ValueError('Age is not integer')

   def __set_name__(self, owner, name):
       self.name = name


class Person:
   name = OnlyASCII()
   age= IntegerField()

   def __init__(self, name, age):
       self.name = name
       self.age = age

person = Person('Oleksii', 29)
print(person.name)
print(person.age)
person.name = 'Mitiev'
person.age = 30
print(person.name)
print(person.age)
person.name = 'Олексій'
person.age = 29.9166666666666667
print(person.name)
print(person.age)
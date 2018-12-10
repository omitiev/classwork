'''

реализовать дескриптор Celsius для преобразования градусов фаренгейта в градусы цельсия
class Temperature:

   celsius = Celsius()

   def __init__(self, initial):
       self.fahrenheit = initial

Для перевода температуры из шкалы Фаренгейта в шкалу Цельсия нужно от исходного числа отнять 32 и умножить результат на 5/9. ((f-32) / 1.8)
Для перевода температуры из шкалы Цельсия в шкалу Фаренгейта нужно умножить исходное число на 9/5 и прибавить 32. (c * 1.8 + 32)
100 = 37.78

'''


class Celsius:
    def __get__(self, instance, owner):
        return (float(instance.fahrenheit) - 32) / 1.8

    def __set__(self, instance, value):
        instance.fahrenheit = float(value) * 1.8 + 32
        return instance.fahrenheit


class Temperature:
    celsius = Celsius()

    def __init__(self, initial):
        self.fahrenheit = initial

    def transform_to_celsius(self, obj):
        self.celsius = obj


temp = Temperature(100)
print(temp.fahrenheit)
print(temp.celsius)
temp.celsius = 37.78
print(temp.fahrenheit)
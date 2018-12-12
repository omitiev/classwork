"""
задачка на использование @property
создать класс

class Distance:
   pass

Distance умеет принимать расстояние в метрах
и содержит атрибуты для конвертации этого значения в
# футы
# шаги
# парсеки

distance = Distance()
distance.metres = 1000.0
# футы
distance.in_feet
3280.8399
# шаги (допустим что в 1 метре 2 шага)
distance.in_steps
2000
# парсеки https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D1%80%D1%81%D0%B5%D0%BA
distance.in_parsecs
3.24078e-14

# значение можно задавать прямо через атрибуты в метрах
distance.in_feet = 1000 # 1000 метров

distance.in_feet
3280.8399

"""


class Distance:
   def __init__(self, meters):
       self._meters = meters

   @property
   def meters (self):
       return self._meters

   @meters.setter
   def meters(self, new_meters):
       if new_meters >= 0:
           self._meters = new_meters

   @property
   def in_feet (self):
       return self._meters * 3.28084

   @in_feet.setter
   def in_feet(self, new_meters):
       if new_meters >= 0:
           self._meters = new_meters

   @property
   def in_steps(self):
       return self._meters * 2

   @in_feet.setter
   def in_step(self, new_meters):
       if new_meters >= 0:
           self._meters = new_meters

   @property
   def in_parsecs(self):
       return self._meters * 3.24077928966636E-17

   @in_parsecs.setter
   def in_parsecs(self, new_meters):
       if new_meters >= 0:
           self._meters = new_meters


distance = Distance(1000)
print(distance.meters)
print(distance.in_feet)
print(distance.in_steps)
print(distance.in_parsecs)

distance.in_feet = 1000
print(distance.in_feet)


distance.in_parsecs = 2000
print(distance.in_parsecs)

import lesson_conditions
import random

for i in range(5):
    print("Hello world", i)
print(i)

# for i in range(101):
#     print(i)

for i in range(101):
    if i%2 == 0:
        print(i)


# i = 1
# while i<=100:
#     print("Hello world", i)
#     i = i+1

for i in range(2100):
    if lesson_conditions.is_leap_year(i):
        print("Leap year", i)

# range - function which creates the range from 0 up to set value-1
# r = range(10)
# r
# range (0,10)
# list (r)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10,0,-2):
    print(i)

for i in "abcdefghijkl":
    print(i)

for i in range(101, 200, 2):
    print(i)

s = "Бронируйте онлайн, платите в отеле‎ Забронируйте отели в Сплите‎‎. Типы: ‎Отели‎, Апартаменты‎, Виллы‎, Хостелы‎, Курортные отели‎, Постель и завтрак‎"

print("Capitals in %s:" % s)
for char in s:
    if char.isupper():
        print(char)

print("Punctual in %s:" % s)
for char in s:
    if char in ",.!;:?":
        print(char)

num_spaces = 0
print("Spaces in %s:" % s)
for char in s:
    if char.isspace():
        num_spaces += 1
print("Number of spaces: %i" % num_spaces)

num_summ = 0
for i in range(101):
    num_summ += i
print("Total summ:", num_summ)

num_summ = 0
for i in range (100):
    num = random.randint(100, 200)
    print(num)
    num_summ += num
print(num_summ)

def sum_random_numbers(min_v, max_v, num_of_numbers):
    num_summ = 0
    for i in range(num_of_numbers):
        num = random.randint(min_v, max_v)
        print(num)
        num_summ += num
    return print("Total summ:", num_summ)

sum_random_numbers(0, 100, 100)
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


def sum_random_numbers(num_of_numbers, lower_bound=100, upper_bound=200):
    num_summ = 0
    for i in range(num_of_numbers):
        num = random.randint(lower_bound, upper_bound)
        print(num)
        num_summ += num
    return num_summ

print("Total summ:", sum_random_numbers(100, 10, 20))


def max_random_numbers(num_of_numbers, lower_bound=100, upper_bound=200):
    curr_max = lower_bound
    for i in range(num_of_numbers):
        num = random.randint(lower_bound, upper_bound)
        print(num)
        if num > curr_max:
            curr_max = num
    return curr_max

print("-----")
result = max_random_numbers(10, 10, 20)
print("answer: ", result)

def min_random_numbers(num_of_numbers, lower_bound=100, upper_bound=200):
    curr_min = upper_bound
    for i in range(num_of_numbers):
        num = random.randint(lower_bound, upper_bound)
        print(num)
        if num < curr_min:
            curr_min = num
    return curr_min

print("-----")
result = min_random_numbers(10, -10, 20)
print("answer: ", result)


print("---------- while ----------")

# def fill_track (max_volume, min_box_volume, max_box_volume):
#     total_volume = 0
#     while total_volume < max_volume:
#         free_space = max_box_volume - total_volume
#         box_volume = random.randint(min_box_volume, max_box_volume)
#         if free_space >= box_volume:
#             total_volume += box_volume
#             print("box vol: %d total: %d " % (box_volume, total_volume))
#         else:
#             print("Last box skiped = %d" % box_volume)
#     return total_volume
#
#
# print("result:" , fill_track(100, 1, 15))
#
def fill_track (max_volume, min_box_volume, max_box_volume):
    total_volume = 0
    free_space = max_volume
    while free_space > 0 :
        box_volume = random.randint(min_box_volume, max_box_volume)
        if free_space >= box_volume:
            free_space -= box_volume
            total_volume += box_volume
            print("box vol: %d total: %d " % (box_volume, total_volume))
        else:
            print("Last box skiped = %d" % box_volume)
    return total_volume

s = input("enter value (e.g.: 2, 2, 2):").split(',')
print("result:", fill_track(int(s[0]), int(s[1]), int(s[2])))


print("hello")
print("1: fun")
print("2: less fun")
print("3: without fun")

# print("Make the choice [1..3], q - exit")

while True:
    choice = input("Make the choice [1..3], q - exit")
    if choice == 'q':
        print("see you next time")
        break
    choice = int(choice)

    if 1 <= choice <= 3:
        if choice == 1:
            print("take your fun")
        if choice == 2:
            print("take less fun")
        if choice == 3:
            print("why so serious?")
    else:
        print("repeat choice")

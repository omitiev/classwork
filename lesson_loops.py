import lesson_conditions

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

for i in range(0,10,2):
    print(i)

for i in "abcdefghijkl":
    print(i)
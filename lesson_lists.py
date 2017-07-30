lst = [10, 20, 30, 40, 50, 60, 70]
print(lst[0])
print(lst[1])
print(lst[2])
print('------')
for i in range (3):
    print(lst[i])

print('------')
for i in range (2, 7):
    print(lst[i])

print('------')
for i in range (len(lst)):
    print(lst[i])

print('------')
for i in range (len(lst)):
    print(lst[i])
    lst[i] *= 2
print(lst)


print('------')
for i in range (len(lst)):
    print(lst[i])
    lst[i] **= 2
print(lst)



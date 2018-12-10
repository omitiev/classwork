lst = [10, 20, 30, 40, 50, 60, 70]
print(lst[0])
print(lst[1])
print(lst[2])
print('------')
for i in range(3):
    print(lst[i])

print('------')
for i in range(2, 7):
    print(lst[i])

print('------')
for i in range(len(lst)):
    print(lst[i])

print('------')
for i in range(len(lst)):
    print(lst[i])
    lst[i] *= 2
print(lst)


print('------')
for i in range(len(lst)):
    print(lst[i])
    lst[i] **= 2
print(lst)

print('------')
for i in range(len(lst) -1,-1,-1):
    print("%d of %d" % ((i), len(lst)))
    if not lst[i]%3:
    # if lst[i] % 3 == 0:
        del lst[i]

print(lst)

def delete_elements_by_condition(lst, condition):
    for i in range(len(lst) - 1, -1, -1):
        print("%d of %d" % ((i), len(lst)))
        if not lst[i] % 3:
            del lst[i]

def is_odd(num):
    return num%2!=0

lst.append(3)
print(lst)
delete_elements_by_condition(lst, is_odd)
print(lst)


def filter_elements_by_condition(lst, condition):
    result = []
    for i in range(len(lst)):
        print("%d of %d" % ((i), len(lst)))
        if condition (lst[i]):
            result.append(lst[i])



# def add(a, b):
#     return a+b
# def mult(a, b):
#     return a*b
# def action(func, a, b):
#     return func(a, b)
#
# s = '2+3'
# eval(s)
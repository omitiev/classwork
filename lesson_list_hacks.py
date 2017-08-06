import math
import string
import random

# list comprehentions
lst = [i for i in range (1, 101)]
print(lst)

lst = [i**2 for i in range (1, 101) if not (i**2)%5]
print(lst)

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(alphabet)
print(list(string.ascii_lowercase))
print([c for c in string.ascii_lowercase])

lst = ['1', '2', '3']
lst2 = [int(elem) for elem in lst]
print(lst2)

results = [round(math.cos(d*180/math.pi), 3) for d in [40, 45, 60]]
print(results)

s = "This is a string"

vowels = [c for c in s if c in 'aoiuey']
print(vowels)
print(' '.join(vowels))


lst_digits = [d for d in range(10)]
print(lst_digits)
print(string.digits)
print(''.join([str(elem) for elem in lst_digits]))


lst_digits = [d for d in range(10)]
print(lst_digits)
lst_digits2 = [i**2 for i in [d for d in range(10)]]
print(lst_digits2)


n = 3
m = 5
matrix = [[0]*n for i in range(m)]
print(matrix)
matrix2 = [[random.randint(1,10) for j in range(n)]for i in range(m)]
print(matrix2)

text1 = "aaa bbb ccc"
text2 = "bbb ccc ddd"
text_lst1 = text1.split()
text_lst2 = text2.split()

result = []
for word in text_lst1:
    if word in text_lst2:
        # result.append(word)
        result += [word]
print(result)


result2 = [word for word in text1.split() if word in text2.split()]
print(result2)


# list functions

lst = [i for i in range(1, 101)]
print(lst)
print(sum(lst))
print(sum([int(i) for i in ['1', '2', '3']]))
print(min([random.randint(10,200) for i in range(100)]))


# lst = list(input("Please enter a min, max, and range (e.g. 2, 15, 100 ): "))
# print(max([random.randint(int(lst[0]), int(lst[1])) for i in range(int(lst[2])]))

##### TUPLE
def foo():
    return 1, 2

x, y = foo()
print(x, y)
t = foo()
print(t, type(t))

def foo (*args):
    print(type(args), args)
    for arg in args:
        print(arg, type(arg))

foo(1)
foo(1,2)
foo(1,2,"3")

var = (4,)
print((type(var)))


def fibonacci_number(n):
    if n == 0:
        return  1
    elif n ==1:
        return  1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

print(fibonacci_number(7))

# map, labda, filter

def func(a):
    return a+1

result = list(map(func, [1, 2, 3]))

print(result)

for elem in result:
    print(elem)

lst1 = list(map(lambda x: x+2, [1, 2, 3]))
print(lst1)

lst2 = list(filter(lambda x: x%2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(lst2)

lst3 = list(map(lambda x: x**2,
                filter(lambda x: not x%2,
                       [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(lst3)


row = 'Wellcom2Hillel'

row2 = list(map(lambda x: ord(x),
                filter(lambda x: x.isupper(), row)))

print(row2)

p_lst = ['mercury', 'mars', 'earth', 'venus']

def get_lenght(s):
    return len(s)

print(p_lst)
p_lst.sort(key=lambda elem: len(elem), reverse=False)
print(p_lst)


print(p_lst)
p_lst.sort(key=len, reverse=True)
print(p_lst)


n_list  = [1, 2, 3, -4, 5, -11, 3, -5, 7, 88, -12]
print(n_list)
n_list.sort(key=abs)
print(n_list)

students = [
    ['Тимченко Дмитрий', '23', 'dmt.tym@gmail.com'],
    ['Юношев Павел', '3', 'p.n.yunoshev@gmail.com'],
    ['Лукшин Евгений', '31', 'otis01990@gmail.com'],
    ['Сеченова Анна', '6', 'sechenovaanna@gmail.com'],
    ['Квято Сергей', '31', 'skvantos@gmail.com'],
    ['Кань Евгений', '4', 'suckrat.us1337@gmail.com'],
    ['Лавренко Евгений', '25', 'superlavrik@gmail.com'],
    ['Кирсанов Илья', '29', 'ilya.kirsanov@gmail.com'],
    ['Жолондковский Вадим', '16', 'vadymzholondkovskiy@gmail.com'],
    ['Марченко Вадим', '25', 'wardomir@gmail.com'],
    ['Митев Алексей', '28', 'oleksii.mitiev@gmail.com'],
    ['Якутко Анастасия', '16', 'anastasiia.yakutko@gmail.com'],
    ['Каменцев Никита', '26', 'niqkamentsev@gmail.com'],
    ['Белоус Екатерина', '17', 'katherinebilous@gmail.com'],
    ['Друмов Вадим', '6', 'vkdrumov@gmail.com']
]

print(students)

p_lst2 = [['mercury', 123], ['mars', 3450], ['earth', 1910], ['earth', 1900], ['venus', 4500]]
p_lst2.sort(key=lambda elem: elem[1])
print(p_lst2)
p_lst2.sort(key=lambda elem: (len(elem[0]), elem[0], elem[1]))
print(p_lst2)
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
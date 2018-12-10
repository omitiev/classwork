# 1. Cделать список  N-й вложенности плоским, например:
# ```def flatten([1,2,3, [4,5,6, [7,8,9]], 10]) -> [1,2,3,4,5,6,7,8,9,10]```


def flatten(items):
    try:
        first, *rest = items
        return flatten(first) + flatten(rest)
    except TypeError:
        return [items]
    except ValueError:
        return []
print('===================')
print(flatten([1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11]]], 12]))
print('===================')

# 2. Реализовать функцию `take(n, iterable)` которая возвщарает первые `n` элементов от итерируемого.


def take(n, iterable):
    return iterable[:n]

print('===================')
print(take(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(take(4, ['test', 2, (4, 5, 9), 4, {'a': 14, 'b': 'est'}, 6, 7, 8, 9, 10]))
print(take(4, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(take(4, [1, 2, 3]))
print('===================')


# 3. Реализовать `zip`. Реализовать `zip` с помощью `map`. (edited)


def new_zip(*args):
    return tuple(tuple(arg[i] for arg in args) for i in range(len(min(args))))

# def map(func, iterables):
#     return [func(elem) for elem in iterables]
# print(map(lambda a: a+1, range(5)))

# def map_zip(*args):



print('===================')
print(tuple(zip([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# print(tuple(zip((1, 2, 3, 4, 5), ['test', 2, (4, 5, 9), 4, {'a': 14, 'b': 'est'}, 6, 7, 8, 9, 10])))
# print(tuple(zip([12, 2, 2, 2, 2], (1, 2, 3, 4))))
print(new_zip([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(new_zip((1, 2, 3, 4, 5), ['test', 2, (4, 5, 9), 4, {'a': 14, 'b': 'est'}, 6, 7, 8, 9, 10]))
# print(new_zip([12, 2, 2, 2, 2], (1, 2, 3, 4)))
print(map_zip([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print('===================')
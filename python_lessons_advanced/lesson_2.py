def map(func, iterables):
    return [func(elem) for elem in iterables]

print(map(lambda a: a+1, range(5)))


def filter(iterables, func=None):
    func = func if func else bool
    if func:
        return [i for i in iterables if func(i) is True]


print(filter([-1, -2, 3, 4], lambda x: x > 0))
print(filter(["", {}, 3, 4], None))


a = [[1,2,3], [4,5,6], [8,9,10]]
*rest, (*rest, last) = [[1,2,3], [4,5,6], [8,9,10]]
print(last)

word_list = ["aaa", "baaa", "acacac"]

b = [i for i in word_list if i.startswith('a')]
print(b)

def is_sum_of_two(digits, value):
    for i in digits:
        if value - i in digits and value - i != i:
            return True
    return False


x = [1, 2, 3, 4, 5, 6, 7]

print(is_sum_of_two(x, 12))


def new_sum(digits, results={}):
    if str(digits) not in results.keys():
        results[str(digits)] = sum(digits)
    return results[str(digits)]

print(new_sum(x))


def is_pal(text):
    return True if str(text) == (str(text)[::-1]) else False

print(is_pal(12321))
import functools

def new_filter(func, iterable):
    func = func if func is not None else bool
    for item in iterable:
        if func(item):
            yield item

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(new_filter(lambda x: x % 2 == 0, a))

print(a)
print(b)

a = [1, 2, 3, '', 4, 5, [], 6, 7, 8, 9]
b = list(new_filter(None, a))

print(a)
print(b)


enumerate("abcde")
print(list(enumerate("abcde")))

def new_enumerate(iterable):
    for item in iterable:
        yield (iterable.index(item), item)

print(list(new_enumerate("abcde")))

def new_enumerate(iterable):
    it = iter(iterable)
    for i in range (len(iterable)):
        yield (i, next(it))

print(list(new_enumerate("abcde")))


def new_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, None)
            if elem is None:
                return
            result.append(elem)
            print(result)
        yield tuple(result)


# def new_zip(*args):
#     return tuple(tuple(arg[i] for arg in args) for i in range(len(min(args))))
print("new_zip")
print(list(new_zip([1,2,3,], "abcde", range(5))))



def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res
    return wrapper

@coroutine
def echo():
    while True:
        boo = yield
        if boo:
            print(boo * 3)


e = echo()
e.send("test")

@coroutine
def bar(target):
    yield from target()

b = bar(echo)
b.send("rest")
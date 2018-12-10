import functools
from functools import lru_cache


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

def item(x):
    return x


print(trace(item(42)))


def profiled(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1
        return func(*args, **kwargs)

    inner.ncalls = 0
    return inner

@profiled
def item(x):
    return x

item(42)
print(item.ncalls)


def humb(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@humb
def beef():
    return "beef"

print(beef())
print(beef.__name__)


print('===================')

def humb(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return wrapper

@humb
def beef():
    return "beef"

print(beef())
print(beef.__name__)


print('===================')


def humb(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = "bread {} bread"
        return result.format(func(*args, **kwargs))
    return wrapper

@humb
def beef():
    return "beef"

print(beef())


print('===================')


def humb(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = "bread {} bread"
        return result.format(func(*args, **kwargs))
    return wrapper

@humb
def beef():
    return "beef"

# the same as example bellow

def x():
    return 'xxxx'


x = humb(x)


print(beef())
print(x())


print('===================')


def humb(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = "bread {} bread"
        wrapper.ncalls += 1
        return result.format(func(*args, **kwargs))
    wrapper.ncalls = 0
    return wrapper

@humb
def beef():
    return "beef"

print(beef())
print(beef())
print(beef.ncalls)

print('===================')


@lru_cache(maxsize = 64)
def test(x):
   return x

print(test(42))
print(test(42))
print(test(42))
print(test.cache_info())

print('===========PRACTICE===========')


def pre(cond, message):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper
    return deco



def squared(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2  # dummy() **2 > 42 ** 2
    return wrapper



@squared
@pre(lambda x: isinstance(x, int), "not a number")
def dummy(num):
    return num

print(dummy(42))
# print(dummy('test'))


print('====================================')

def pre(cond, message):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper
    return deco



def squared(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return list(map(lambda x: x ** 2, func(*args, **kwargs)))
    return wrapper



@squared
@pre(lambda *args: all([isinstance(x, int) for x in args]), "not a number")
def dummy(*args):
    return args

print(dummy(42, 42, 42, 42, 42))


print('====================================')

def pre(cond, message):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper
    return deco



def squared(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return list(map(lambda x: x ** 2, func(*args, **kwargs)))
    return wrapper


def last_cal(func):
    def wrapper(*args, **kwargs):
        wrapper.last_call = func(*args, **kwargs)
        return func(*args, **kwargs)
    wrapper.last_call = 'not called'
    return wrapper

@last_cal
@squared
@pre(lambda *args: all([isinstance(x, int) for x in args]), "not a number")
def dummy(*args):
    return args

print(dummy(*range(10)))
print(dummy.last_call)
print(dummy(*range(11)))
print(dummy.last_call)



print('=================TEACHER====================')

def pre(cond, message):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)

        return wrapper

    return deco


def squared(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return list(map(lambda x: x ** 2, func(*args, **kwargs)))

    return inner


def last_call(func):
    def inner(*args, **kwargs):
        inner.last_args = args
        return func(*args, **kwargs)

    def last_call():
        return f"last call info: args {inner.last_args}"

    inner.last_args = "not called"
    inner.last_call = last_call
    return inner


@last_call
@squared
@pre(lambda *args: all([isinstance(num, int) for num in args]),
     "not a number")
def dummy(*args):
    return args


print(dummy(*range(10)))
print(dummy.last_call())

# dummy.last_call() -> "last call info: args [0,1,2,3,4,5,6,7,8,9]"
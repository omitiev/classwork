# f = open(r'/home/oleksii/Documents/file_test.txt')
# d = {"UA":"Kyiv"}
# print(d['UA'])
# #....
# #....
# f.close()
import time

class MgrContextTest:

    def __init__(self):
        pass

    def __enter__(self):
        print("Entered")

    def __exit__(self, *exc_info):
        print("Exited")

# with MgrContextTest() as mgr_test:
#     print("I'm inside with body")
#     v = 1/0
#
#
# with open(r'/home/oleksii/Documents/file_test.txt') as f:
#     print(f.read())



for x in range(1, 10, 2):
    print(x)


class frange:

    class frange_iterator:

        def __init__(self, start, stop, step=1):
            self.current = None
            self.start = start
            self.stop = stop
            self.step = step

        def __next__(self):
            if self.current is None:
                self.current = self.start
                return self.current
            elif self.current + self.step <= self.stop -1:
                self.current += self.step
                return self.current
            else:
                raise StopIteration("frange is exhausted")


    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step


    def __iter__(self):
        return frange.frange_iterator(self.start,
                                      self.stop,
                                      self.step)



for x in frange(1, 10, 2.5):
    print(x)

print(len(list(frange(1, 10, 2.5))))

def perf_meter_v2(func):

    def inner(*args):
        start = time.time()
        result = func(*args)
        print(time.time() - start)
        return result
    return inner


def cache_it(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner

@cache_it
@perf_meter_v2
def foo(n):
    time.sleep(n)
    return n*42

@perf_meter_v2
def is_sorted(iterable):
    result = iterable == sorted(iterable)
    return result

result = is_sorted([1,2,3,4,5])
print(result)

result = is_sorted([1,2,3,4,1])
print(result)

# assert is_sorted([1,2,3,4,5]) == True
# assert is_sorted([1,2,3,4,1]) == True

@perf_meter_v2
def is_sorted_v2(iterable):
    it = iter(iterable)
    it2 = iter(iterable)
    next(it2)
    # print(list(zip(it, it2)))
    result = all(map(lambda t: t[0] <= t[1], (zip(it, it2))))
    return result
    # all - vse elementi iteratora = True
    # any - naoborot

    # return iterable == sorted(iterable)

print(is_sorted_v2([1, 2, 3, 4, 5]))
print("NEW")
# assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]) == False
# assert is_sorted_v2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]) == False
# assert is_sorted_v2([1,2,3,4,1]) == True




# def perf_meter(func):
#     start = time.time()
#     func()
#     print(time.time() - start)
#
# print('NEW+++++++++')
#
# perf_meter(foo)



print('NEW2++++++++')
# foo = perf_meter_v2(foo)
foo(1)
print('NEW3++++++++')
foo(1)

print('NEW4++++++++')
# assert is_sorted([1, 2, 3, 4, 5]) == True
# assert is_sorted_v2([1, 2, 3, 4, 5]) == True

print('NEW5++++++++')
result1 = foo(2)
result2 = foo(2)
print(result1, result2)
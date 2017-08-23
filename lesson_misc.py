# f = open(r'/home/oleksii/Documents/file_test.txt')
# d = {"UA":"Kyiv"}
# print(d['UA'])
# #....
# #....
# f.close()

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
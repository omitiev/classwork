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

with MgrContextTest() as mgr_test:
    print("I'm inside with body")
    v = 1/0


with open(r'/home/oleksii/Documents/file_test.txt') as f:
    print(f.read())

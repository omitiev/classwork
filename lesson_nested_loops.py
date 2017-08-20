# for i in range(10):
#     for j in range(10):
#         for k in range(10):

for i in range(10):
    print("%d: " % i, end="")
    for j in range(10):
        print("%d" % j, end="")
    print()


def pyph_table(n=9, m=9):
    for i in range(1, n+1):
        # print("%d: " % i, end="")
        for j in range(1, m+1):
            print("%d" % (i*j), end="\t")
        print()

pyph_table(9, 9)
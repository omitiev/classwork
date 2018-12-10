# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149

import default


default.start(26)


def primes(x):
    primes_lst = [2]
    for i in range(3, x+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in primes_lst:
            if j * j - 1 > i:
                primes_lst.append(i)
                break
            elif i % j == 0:
                break
        else:
            primes_lst.append(i)
    return primes_lst


num = int(input("Please enter an upper bound for the range (e.g. 100): "))
print("The primes in your range are: %s " % (primes(num)))


default.end()

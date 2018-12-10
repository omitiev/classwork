import random


def start(task):
    print('='*70)
    print('Task', task)
    print('='*70)


def end():
    print('=' * 70)
    print('This task was decided by Oleksii Mitiev. Thank you for your attention.')
    print('=' * 70)


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 != 0


def random_list(list1):
    list2 = list(set(list1))
    random.shuffle(list2)
    return list2


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


def select_random(lst1, num):
    i = 0
    lst2 = []
    while i < num:
        lst2.append(random.choice(lst1))
        i += 1
    return lst2


def create_random_lst(lst_len):
    i = 0
    lst = []
    while i < lst_len:
        lst.append(random.randint(-1000, 1000))
        i += 1
    return lst

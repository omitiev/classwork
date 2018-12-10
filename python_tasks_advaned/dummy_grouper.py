import itertools

'''

Данный пример групирует входящий список по n элементов
def dummy_grouper(data, n):
    groups_count = len(data) // n
    return [tuple(data[i*n:(i+1)*n]) for i in range(groups_count)]
test_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dummy_grouper(test_num_list, 2)
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

Предлагается, ускорить ее работу, используя генераторы\модуль itertools.

В качестве точки отсчета при оптимизации - брать такую группировку
dummy_grouper(range(100000000), 10)
(убедитесь что есть 2 и более гб свободной оперативной памяти)

$ gtime -f "Memory used (kB): %M\nUser time (seconds): %U" python dummy_grouper.py

Memory used (kB): 2111668
User time (seconds): 14.21

Сейчас она выполняется за 14 секунд, потребляя 2 гб.


С помощью itertools можно добиться значительных успехов:
gtime -f "Memory used (kB): %M\nUser time (seconds): %U" python smart_grouper.py

Memory used (kB): 6900
User time (seconds): 2.31

'''

def dummy_grouper(data, n):
    groups_count = len(data) // n
    return [tuple(data[i*n:(i+1)*n]) for i in range(groups_count)]
test_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(dummy_grouper(test_num_list, 2))
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# dummy_grouper(range(100000000), 10)


def smart_grouper(data, n):
    iterator = iter(data)
    for i in range(len(data // n)):
        yield (i,next(iterator))

print(list(smart_grouper(test_num_list, 2)))


# def new_enumerate(iterable):
#     it = iter(iterable)
#     for i in range (len(iterable)):
#         yield (i, next(it))
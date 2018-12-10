# 8. В одномерном массиве поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.

import default
import copy


default.start(8)


def replace_min_max_values(lst1):
    lst2 = copy.deepcopy(lst1)
    lst2[lst1.index(max(lst1))] = min(lst1)
    lst2[lst1.index(min(lst1))] = max(lst1)
    return lst2


base_lst = default.select_random(default.primes(1000), 10)
print("Base lst is: ", base_lst)
base_lst = replace_min_max_values(base_lst)
print("The new lst is: ", base_lst)


default.end()

# 6. Создать список из 10 любых простых чисел, записанных в случайном порядке.

import default


default.start(6)


lst1 = default.primes(1000)
print("My random list is: ", default.select_random(lst1, 10))


default.end()

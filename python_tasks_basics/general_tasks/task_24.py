# Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
# Пользователь вводит число,а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
# После чего опять просит угадать. И так пока пользователь не угадает выбранное число.

import default
import random

default.start(24)

print("""
Hello!
I've chosen the number from 1 to 10.
Do you want to guess it?
""")
answer = input("Press Y if yes, or N if not:")
if answer == 'Y' or answer == 'y':
    d = random.randint(1, 10)
    while True:
        choice = input("Make the choice [1..10], q - exit")
        if choice == 'q':
            print("OK. See you next time")
            break
        choice = int(choice)

        if 1 <= choice <= 10:
            if choice < d:
                print("My number is bigger than yours :)")
            if choice > d:
                print("My number is smaller than yours :)")
            if choice == d:
                print("Correct! My number is %i" % (d))
                print("I think this is all for today. Come tomorrow :)")
                break
        else:
            print("Wrong value, please repeat your choice")
elif answer == 'N' or answer == 'n':
    print("Ok. Maybe next time ...")
else:
    print("Something went wrong, please observe your answer")


default.end()

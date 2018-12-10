# 4. Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры

import default


default.start(4)


def multipy_odds(number):
        x = 1
        nums = list(number)
        # x = [int(i)*=x for i in nums if default.is_odd(int(i))]
        for i in nums:
            if default.is_odd(int(i)):
                x *= int(i)
        if x > 1:
            return x
        elif x == 1 and '1' in number:
            return 1
        else:
            return 0

number = str(input("Please enter a number with 5 digits: "))
if len(number) == 5:
    print("Your number is:", number)
    if multipy_odds(number) >= 1:
        print("The multiplication of all odd digits in number is %d" % (multipy_odds(number)))
    else:
        print("Your number doesn't contain odd digits")
else:
    print("Something went wrong, please observe your number")

default.end()

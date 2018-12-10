# Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
# Пароль состоит из 8 символов
# В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# Пароль обязательно должен содержать Большие и маленькие буквы и цифры

import default
import random


default.start(31)


def create_rand_pswd(pswd_length):
    lst_of_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lst_of_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    lst_of_nums = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    mutual_lst = lst_of_upper + lst_of_lower + lst_of_nums
    pswd_chr_lst = ['_']
    i = 1
    while i < (pswd_length-3):
        pswd_chr_lst.append(random.choice(mutual_lst))
        i += 1
    pswd_chr_lst += random.choice(lst_of_upper)+random.choice(lst_of_lower)+random.choice(lst_of_nums)
    random.shuffle(pswd_chr_lst)
    return pswd_chr_lst


answer = input("Press Y if yes, or N if not:")
if answer == 'Y' or answer == 'y':
    length = int(input("Please enter the length for your password (e.g. 8):"))
    if length > 0:
        print("Your new password is %s" % (''.join(create_rand_pswd(length))))
    else:
        print("Something went wrong, please observe your answer")
elif answer == 'N' or answer == 'n':
    print("Ok. Maybe next time ...")
else:
    print("Something went wrong, please observe your answer")


default.end()

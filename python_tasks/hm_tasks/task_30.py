# Создать программу, которая запрашивает у пользователя произвольную строку символов.
# Далее программа ее шифрует и выводит на экран в зашифрованном виде.
# Шифрование происходит путем замены каждого символа символом, который находится на 5 позиций правее в предопределенной таблице шифрования.
# Таблица шифрования задается программистом в виде одномерного списка символов.
# Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу.
# 	Например: Таблица шифрования (а,б,в,г,д,о,1,2,3,4,5,6,-,0)
# 	Исходная строка, которую ввел пользователь: год-2016
# 	Зашифрованная строка, которую выдала программа: 354г-д6в
# 	Примечание: т.н. таблица шифрования может быть представлена как строка или список.


import default


default.start(30)


def encrypt_my_text(base_str):
    crypto_table = [chr(i) for i in range(ord('A'), ord('z') + 1)] + [chr(i) for i in range(ord('!'), ord('?') + 1)]
    encrypted_list = []
    for i in base_str:
        char_ind = (crypto_table.index(i) + 5) % len(crypto_table)
        encrypted_list.append(crypto_table[char_ind])
    return encrypted_list


usr_str = input("Please enter your string for encrypting: ")
print("Now your string is encrypted: ", "".join(encrypt_my_text(usr_str)))


default.end()

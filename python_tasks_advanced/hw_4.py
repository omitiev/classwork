"""
Домашнее задание, необходимо реализовать 2 функции - encode и decode, которые реализуют вашу собственную кодировку.

например
```my_text_input = 'blabla'
encoded_text = encode(my_text_input, 'MY_SECRET_KEY')
print(encoded_text) -> 'pdxpdx'
decoded_text = decode(encoded_text, 'MY_SECRET_KEY')
print(decoded_text) -> 'blabla'```
важный нюанс, кодирование последовательности при одном и том же ключе не должно меняться, 
т.е. `encode(my_text_input, 'MY_SECRET_KEY')` при одном и том же ключе всегда будет возвращать закодированную 
строку `pdxpdx` (результат кодирования естественно будет зависеть от вашей реализации)

модули\библиотеки, которые могут облегчить реализацию задачи
модуль - `string`
модуль - `random`
"""
import random
import string


def enigma():
    print('Hello. \nENIGMA is turned on. \n')

    while True:
        action = input('Options: \n'
                       'Encoding - press E\n'
                       'Decoding - press D\n'
                       'Exit - press X\n'
                       '>>> ')

        if action.lower() == 'e':
            text, password = get_data()
            encode(text, password)

        elif action.lower() == 'd':
            text, password = get_data()
            decode(text, password)

        elif action.lower() == 'x':
            break

        else:
            print("Your choice isn't clear.\n")

    print('Goodbye.\nENIGMA is turned off.')

def get_data():
    text = input('Please enter the text for encoding / decoding\n'
                 '>>> ')
    password = input('Please enter the password\n'
                     '>>> ')
    return text, password

def encode(text_input, password):
    length = round(len(text_input) / len(password)) if round(len(text_input) / len(password)) > 0 else 1
    long_password = password * length
    result = ''.join([chr(i) for i in list(map(lambda x: ord(x[0]) + ord(x[1]), zip(text_input, long_password)))])
    print("Result => {result}\n".format(result=result))
    return result

def decode(encoded_test, password):
    try:
        length = round(len(encoded_test) / len(password)) if round(len(encoded_test) / len(password)) > 0 else 1
        long_password = password * length
        result = ''.join([chr(i) for i in list(map(lambda x: ord(x[0]) - ord(x[1]), zip(encoded_test, long_password)))])
        print("Result => {result}\n".format(result=result))
        return result
    except ValueError:
        result = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.choice(range(25)))])
        print("Result => {result}\n".format(result=result))
    return result

enigma()
# german_key = "22"
# alan_turing = "d"
# message = "my secret message"
# my_encoded_secret = encode(message, german_key)
# my_decoded_secret = decode(my_encoded_secret, alan_turing)
# assert message == my_decoded_secret
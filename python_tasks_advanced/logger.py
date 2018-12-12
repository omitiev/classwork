import functools

'''

Задание - представим есть файл с логами, его нужно бессконечно контролировать
на предмет возникнования заданных сигнатур.

Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
печатать результат

Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

Структура пайплайна:
```
def coroutine(*args):
    # your code here


@coroutine
def grep(*args):
	# your code here


@coroutine
def printer():
	# your code here


@coroutine
def dispenser(*args):
    # your code here


def follow(*args):
    # your code here
```

Каждый grep следит за определенной сигнатурой

Как это будет работать:

```
f_open = open('log.txt') # подключаемся к файлу
follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()), # отслеживаем
           grep('is', printer()),     # заданные
           grep('great', printer()),  # сигнатуры
       ])
       )
```
Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть

Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.

Если все плохо - план Б лекция Дэвида Бизли
[warning] решение там тоже есть :)
https://www.dabeaz.com/coroutines/Coroutines.pdf

'''


def coroutine(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res
    return inner


@coroutine
def grep(*args):
    while True:
        line = yield
        if args in line:
            return line


@coroutine
def printer():
    pass


@coroutine
def dispenser(*args):
    pass


def follow(*args):
    # your code here

    f_open = open('log.txt')  # подключаемся к файлу
    follow(f_open,
           # делегируем ивенты
           dispenser([
               grep('python', printer()),  # отслеживаем
               grep('is', printer()),  # заданные
               grep('great', printer()),  # сигнатуры
           ])
           )
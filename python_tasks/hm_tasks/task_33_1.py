'''

33. Для подсчета баллов, набранных студентами группы надо обработать информацию, представленную в виде взаимосвязанных структур данных:
group - список словарей, где словарь описывает информацию о студенте.
hw_results: список с информацией о решенных д/з.
Каждый элемент - это словарь с ключами: id студента, task_completion - список выполненных д/з.
test1_results: список с информацией о решенном Test1.
Каждый элемент - это словарь с ключами: id студента, task_completion - список выполненных заданий
test1_weights: словарь с весами заданий Test1.
Ключ - номер задачи, значение - вес задачи (кол-во баллов, которое начисляется за ее решение).

Между этими данными связь устанавливается с помощью ключа студента. Например, студенту с id=1024, соответствуют домашние задания и задачи из Test1,
у которых ключу “id” соответствует значение 1024 . Связь между весом задачи Test1 и ее номером устанавливается по ключу в словаре test1_weights.

Необходимо написать 2 функции:
update_student_results: обновляет рейтинг студента, на основании предоставленной информации. См. описание ф-ции.
print_student_info: распечатывает информацию о студенте, сортируя по указанному ключу из словаря студента. По умолчанию сортировка по ключу ‘fullname’.

Данные для обработки: https://github.com/dbradul/python/blob/master/class_stats.py

Также можно реализовать эту задачу, получив данные через RestAPI. Пример работы со студентом показан в модуле:
https://github.com/dbradul/python_classes/blob/master/basics/class_stats_v2.py

Установка и работа с библиотекой requests:
http://docs.python-requests.org/en/master/user/install/#pip-install-requests
http://docs.python-requests.org/en/master/

Работа с json:
https://code.tutsplus.com/tutorials/how-to-work-with-json-data-using-python--cms-25758

Примечание:
Формат данных полученных через RestAPI может отличаться. Например, веса заданий контрольной возвращаются в виде списка,
а не словаря, как в модуле class_stats.py

'''


import default


default.start(33)


group = [
    {"id": 1024, "fullname": "Тимченко Дмитрий",    "email": "dmt.tym@gmail.com", "github": "https://github.com/TymDmitriy", "rank": 0},
    {"id": 1025, "fullname": "Юношев Павел",        "email": "p.n.yunoshev@gmail.com", "github": "", "rank": 0},
    {"id": 1026, "fullname": "Лукшин Евгений",      "email": "otis01990@gmail.com", "github": "https://github.com/EugeneSchweiger", "rank": 0},
    {"id": 1027, "fullname": "Сеченова Анна",       "email": "sechenovaanna@gmail.com", "github": "https://github.com/AnnaSechenova", "rank": 0},
    {"id": 1028, "fullname": "Квято Сергей",        "email": "skvantos@gmail.com", "github": "https://github.com/kvantos/", "rank": 0},
    {"id": 1029, "fullname": "Кань Евгений",        "email": "suckrat.us1337@gmail.com", "github": "https://github.com/suckratus", "rank": 0},
    {"id": 1030, "fullname": "Лавренко Евгений",    "email": "superlavrik@gmail.com", "github": "https://github.com/SuperLavrik", "rank": 0},
    {"id": 1031, "fullname": "Кирсанов Илья",       "email": "ilya.kirsanov@gmail.com", "github": "https://github.com/IlyaKirsanov", "rank": 0},
    {"id": 1032, "fullname": "Жолондковский Вадим", "email": "vadymzholondkovskiy@gmail.com", "github": "", "rank": 0},
    {"id": 1033, "fullname": "Марченко Вадим",      "email": "wardomir@gmail.com", "github": "", "rank": 0},
    {"id": 1034, "fullname": "Митев Алексей",       "email": "oleksii.mitiev@gmail.com", "github": "https://github.com/omitiev", "rank": 0},
    {"id": 1035, "fullname": "Якутко Анастасия",    "email": "anastasiia.yakutko@gmail.com", "github": "https://github.com/ayakutko/HW_1_6", "rank": 0},
    {"id": 1036, "fullname": "Каменцев Никита",     "email": "niqkamentsev@gmail.com", "github": "https://github.com/TheNiq", "rank": 0},
    {"id": 1037, "fullname": "Белоус Екатерина",    "email": "katherinebilous@gmail.com", "github": "https://github.com/KateBilous/", "rank": 0},
    {"id": 1038, "fullname": "Друмов Вадим",        "email": "vkdrumov@gmail.com", "github": "https://github.com/Vkdrumov", "rank": 0},
]

hw_results = [
    {"id":1024, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1025, "task_completion": [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1026, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0]},
    {"id":1027, "task_completion": [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1028, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]},
    {"id":1029, "task_completion": [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1030, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1031, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]},
    {"id":1032, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1033, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]},
    {"id":1034, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]},
    {"id":1035, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1036, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0]},
    {"id":1037, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
    {"id":1038, "task_completion": [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},
]


test1_results = [
    {"id": 1024, "task_completion": [1,1,1,1,1,1,1,1,1,1,0,0] },
    {"id": 1025, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1026, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1] },
    {"id": 1027, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1028, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,1] },
    {"id": 1029, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1030, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,1] },
    {"id": 1031, "task_completion": [1,1,1,1,1,1,0,0,0,0,0,0] },
    {"id": 1032, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1033, "task_completion": [1,1,1,1,1,1,1,1,1,1,1,0] },
    {"id": 1034, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1035, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1036, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1037, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
    {"id": 1038, "task_completion": [0,0,0,0,0,0,0,0,0,0,0,0] },
]


test1_weights = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2,
    5 : 2,
    6 : 2,
    7 : 4,
    8 : 4,
    9 : 4,
    10 : 8,
    11 : 8,
    12 : 15
}


def update_students_results(group):
    '''
    Calculate student results and put them into the student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
        sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''
    pass


def print_students_info(group, sort_by_key="fullname"):
    '''
    Prints students info sorted according to the passed key in dictionary). By default, sort by students names.
    Student info should be presented as a card that includes the following information:
        - id,
        - name,
        - email,
        - github account (only name, not URL path)
        - rank
    Example (format is not strictly required):
        -----------------------------------------
        : ID:                               1025:
        :.......................................:
        : Full name:                Юношев Павел:
        : Email:          p.n.yunoshev@gmail.com:
        : Github:                               :
        : Rank:                               42:
        -----------------------------------------
    :return: None
    '''
    pass

if __name__ == "__main__":
    update_students_results(group)
    print_students_info(group, "rank")








default.end()

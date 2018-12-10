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
import requests
import json
from pprint import pprint


default.start(33)

# ------------------------------------------------------------------------------
BASE_URL = "http://54.201.47.219:8080/api"
VERSION = "v1"
URL = "%s/%s" % (BASE_URL, VERSION)


# ------------------------------------------------------------------------------
def log_error(msg):
    print("ERROR: ", msg)


# ------------------------------------------------------------------------------
def get_students():
    response = requests.get(URL + '/students')
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['students']
    else:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def get_student(id):
    response = requests.get(URL + '/students/' + str(id))
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['student']
    else:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def update_student(id, upd_fields):
    response = requests.put(URL + '/students/' + str(id),
                            json=json.dumps(upd_fields))

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def add_student(student):
    response = requests.post(URL + '/students/',
                             json=json.dumps(student))

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def reset():
    response = requests.put(URL + '/reset')

    result = response.status_code == 200

    if not result:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def demo():
    '''
    Demonstrates fetching, updating and adding new student.
    Resets remote DB afterwards
    :return: None
    '''

    ## available urls
    ## http://54.201.47.219:8080/api/v1/students/
    ## http://54.201.47.219:8080/api/v1/students/1025
    # http://54.201.47.219:8080/api/v1/hw_results/
    # http://54.201.47.219:8080/api/v1/hw_results/1025
    # http://54.201.47.219:8080/api/v1/test1_results/
    # http://54.201.47.219:8080/api/v1/test1_results/1025
    # http://54.201.47.219:8080/api/v1/test1_weights/

    # pprint(get_students())
    #
    # pprint(get_student(1024))
    # update_student(1024, {'rank': 42})
    # pprint(get_student(1024))
    #
    # add_student({"id": 1234, "fullname": "AAAA", "email": "x@y.z", "github": "", "rank": 0})
    # pprint(get_student(1234))
    #
    # reset()
    # pprint(get_students())
    # pprint(get_hw_results())
    # pprint(get_test1_results())
    # pprint(get_test1_weights())
    # pprint(update_students_results())
    # pprint(get_students())
    pprint(print_students_info())
    # pprint(get_hw_results(1034))



# ------------------------------------------------------------------------------
def get_hw_results():
    response = requests.get(URL + '/hw_results')
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = {i['id']: i['task_completion'] for i in json_object}
    else:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def get_student_hw_results(id):
    response = requests.get(URL + '/hw_results/' + str(id))
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['task_completion']
    else:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def get_test1_results():
    response = requests.get(URL + '/test1_results')
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = {i['id']: i['task_completion'] for i in json_object}
    else:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def get_test1_weights():
    response = requests.get(URL + '/test1_weights')
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['test1_weights']
    else:
        log_error(response.content)

    return result


# ------------------------------------------------------------------------------
def update_students_results():
    '''
    Calculate student results and put them into the student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
        sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''


    students = get_students()
    hw_result = get_hw_results()
    test1_results = get_test1_results()
    test1_weights = get_test1_weights()
    for student in students:
        s_id = student['id']
        # get_student_hw_results(s_id)     slow method
        hw_rank = hw_result[s_id]
        test1_rank = test1_results[s_id]
        total_rank = sum(hw_rank)
        for i in range(len(test1_rank)):
            total_rank += int(test1_rank[i]) * int(test1_weights[i])
        update_student(s_id, {'rank': total_rank})


# ------------------------------------------------------------------------------
def print_students_info(sort_by_key='fullname'):
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
    students = get_students()
    students.sort(key=lambda student: student[sort_by_key])
    for student in students:
        print('-' * 50)
        print(':' + ' ID: ' + '%43d:' % (student['id']))
        print(':' + '.'*48 + ':')
        print(':' + ' Full name: ' + '%36s:' % (student['fullname']))
        print(':' + ' Email: ' + '%40s:' % (student['email']))
        git = student['github'].split('/')
        if len(git) >=4:
            print(':' + ' Github: ' + '%39s:' % (git[3]))
        else:
            print((':' + ' Github: ' + ' '*10 + 'user doesn\'t have GIT account:'))
        print(':' + ' Rank: ' + '%41d:' % (student['rank']))
        print('-' * 50)


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    demo()

    # update_students_results()
    # print_students_info()


default.end()

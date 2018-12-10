# Задача написать функцию, которая определяет надо ли переводить время на час вперед/назад.
# Должна вернуть +1, если надо переводить вперед, -1, если назад, 0 - если не надо.
# Получает месяц, день недели, день месяца: def daylight_saving (month, week_day, day_of_month)
# last Sundays of March and October

import default


default.start(4)


def daylight_saving (month, week_day, day_of_month):
    if month == 3:
        if week_day == 7:
            if 26 <= day_of_month <= 31:
                return +1
    elif month == 10:
        if week_day == 7:
            if 26 <= day_of_month <= 31:
                return -1
    else:
        return 0

mon = input("Please enter a month:")
w_day = input("Please enter a week day:")
d_of_mon = input("Please enter a day of week:")

print(daylight_saving(mon, w_day, d_of_mon))


default.end()
"""Задача № 1 Написать калькулятор для депозитного вклада.
Функция должна принимать на вход сумму вклада и срок в месяцах.
На выходе должны получать итоговую сумму с учетом вклада.

доход по вкладу = сумма вклада / 100% * % ставку /количество дней в году * количество дней действия вклада

Процентная ставка зависит от срока. 
до 3 (включительно) - 8%,
до 6 (включительно) - 10%,
до 12 - 11%,
год и более - 12%

Выплаты ежемесячные.
На выходе нужно учесть налог на прибыль в 20%."""


def procent(month):
    if month <= 3:
        proc = 0.08
    elif month <= 6:
        proc <= 0.1
    elif month < 12:
        proc = 0.11
    else:
        month >= 0.12
    return proc


def deposit(value, months):
    procent_value = procent(3)
    dep = value / 100 * procent_value / 12 * months
    return dep


print(deposit(10000, 12))


"""Задача № 2
Дано число N. После чего в порядке обхода вводятся N пар координат
многоугольника на плоскости.Необходимо найти периметр этого многоугольника. """


# def repeater():
#     user_input = True
#     while user_input is True:
#         user_input = input('repeat?')
#         if user_input == 'y':
#             user_input = True
#             continue
#         elif user_input == 'n':
#             user_input = False
#         else:
#             print('Моя твоя не понимать!!!')
#             user_input = True
#     return print('THE END')


# repeater()

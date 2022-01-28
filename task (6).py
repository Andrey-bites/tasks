"""Давайте попробуем написать "скелет" ролевой игры. Естественно на ООП)) Для этого понадобятся игровые юниты. В дальнейшем из Юнита наделаем героев (наследованием) и будем устраивать между ними битвы.

Напишите класс Unit, реализуйте в нем атрибуты "имя", "здоровье", "атака", "защита". Обеспечьте передачу в "имя" только строчных данных, в "здоровье", "атака", "защита" - только числовых

Напишите декоратор, замеряющий время выполнения функции

* Модифицируйте декоратор таким образом, чтобы декоратор вместе с ответом функции возвращал строку, содержащую информацию о затраченном на выполнение времени. Формат возвращаемого времени - H-MM-SS-MS (часы-минуты-секунды-милисекунды)"""
import datetime
import time

from markupsafe import re



# class Unit:
#     name = 'Bil'
#     health = 100
#     attack = 10
#     protection = 5

#     def __init__(self, init_name=name, init_health=health, init_attack=attack, init_protection=protection):
#         if isinstance(init_name, str):
#             self.name = init_name

#         if isinstance(init_health, int):
#             self.health = init_health

#         if isinstance(init_attack, int):
#             self.attack = init_attack

#         if isinstance(init_protection, int):
#             self.protection = init_protection


# u1 = Unit()

# print(u1.name)
# print(u1.health)
# print(u1.attack)
# print(u1.protection)



def lead_time(func):

    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        res = func(*args, **kwargs)
        finish = datetime.datetime.now()
        result = finish - start
        print(f'{result} seconds for leed time')
        return res

    return wrapper


@lead_time
def some_function(a, b):
    lst = [x ** 2 for x in range(a, b)]
    
    return lst

print(some_function(1, 1000))


def type_check(tp_of_arrg):
    
    def wrapper(func):
        
        def wrapper1(*args):
            for arg in args:
                if not isinstance(arg, tp_of_arrg):
                    raise ValueError
            return func(*args)
        
        return wrapper1

    return wrapper


@type_check(str)
def some_function(a, b):
    return a, b

print(some_function('2', '3'))

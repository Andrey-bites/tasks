"""HomeWork."""

"""Задание 1. Доделайте последнее задание из практики (email).
Сделайте все проверки и попробуйте оптимизировать."""


"""Задание 2. Дан list произвольных чисел
(напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44]).
Написать программу, которая удалит из него все числа,
которые меньше 18 и больше 81. """

lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44]
lst2 = [i for i in lst if i > 18 and i < 81]
print(lst2)


"""Задание 3.* Напишите программу, которая (аналогично заданию 1)
проанализирует строку на номер телефона.
Правила проверки - "+" впереди и 12 цифр за ним."""

print('Пример номера "+380631122333"')
phone_n = input('Введите номер: ')

if len(phone_n) != 13:
    print('не 13 знаков')
elif phone_n[0] != '+':
    print('Введите в начале номера "+"')
elif phone_n[1] != '3':
    print('Введите в начале номера "+3"')
elif phone_n[2] != '8':
    print('пропустил 8')
elif phone_n[3] != '0':
    print('Пропустил 0!!')
else:
    if phone_n[1:-1].isdigit():
        print('мы вам позвоним!!!')
        print(f'Ваш намер:--------->{phone_n}')
    else:
        print('Ваш номер содержит буквы')


"""Задание 4.** Ввести из консоли строку.
Найти в строке самое длинное слово,
в котором присутствуют подряд две согласные буквы. """

#  There are a number of traditions for weddings that have survived into the 21st century. It is still traditional for the bride and groom to have their own parties the night before getting married. The groom’s party is called a ‘Stag party’, while the bride’s is known as a ‘Hen party’.

txt = input('Enter you text: ')
split_txt = txt.split()
consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                  'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
add_wrd = ''
longest_wrd = ''
counter = 0
""" не закончил 4 задание """

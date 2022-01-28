""" Подключитесь к API НБУ ( https://bank.gov.ua/ua/open-data/api-dev ),
получите текущий курс валют и запишите его в TXT-файл в формате
 "дата создания запроса"
1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
3. [название ввалюты 3] to UAH: [значение курса к валюте 3]
...
n.[название ввалюты n] to UAH: [значение курса к валюте n] """
import requests
import datetime


try:
    responce = requests.get(
        'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
except:
    pass

# print(responce.status_code)  # responce.status_code ?? 200
# print(responce.headers)  # responce.headers 'aplication/json'

try:
    responce.json()
except:
    pass
currency_name = responce.json()


def currency(responce):
    res = ''
    currency_name = responce.json()
    date = datetime.date.today()
    with open('cur.txt', 'w') as f:
        f.write(f'Дата создания запроса: {date} \n')
        for index, key in enumerate(currency_name):
            res += f'{index + 1}. {key["txt"]} to UAH: {key["rate"]} \n'
        f.write(res)


currency(responce)


""" ** Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к этой валюте за указаную дату используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП! """


# class Currency:
#     try:
#         responce = requests.get(
#             'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
#     except:
#         pass

#     def __init__(self, request):
#         self.request = responce

#     def check_request(self, responce):
#         if responce.headers['Content-Type'] == 'application/json; charset=utf-8' and responce.status_code == 200:
#             res = ''
#             currency_name = responce.json()
#             for index, key in enumerate(currency_name):
#                 res += f'{index + 1}. {key["txt"]} to UAH: {key["rate"]} \n'
#             print(res)
#         else:
#             raise Exception

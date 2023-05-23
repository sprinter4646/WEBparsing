# https://stepik.org/lesson/704700/step/3?auth=login&unit=705135
# Используйте полученный по ссылке=http://parsinger.ru/downloads/get_json/res.json JSON,
# чтобы посчитать количество товара в каждой категории.
#
# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общее количество товаров
#
# Количество вы найдёте в каждой карточке товара.


import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url).json()
d = {}
for item in response:
    d[item['categories']] = d.get(item['categories'], 0) + int(item['count'])
print(d)

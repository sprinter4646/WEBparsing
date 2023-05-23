# https://stepik.org/lesson/704700/step/4?auth=login&unit=705135
# Используйте полученный по ссылке=http://parsinger.ru/downloads/get_json/res.json JSON,
# чтобы посчитать стоимость товаров в каждой отдельной категории.
#
# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общая стоимость товаров.


import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url).json()
d = {}
for item in response:
    d[item['categories']] = d.get(item['categories'], 0) + int(item['price'].strip(' руб'))*int(item['count'])
print(d)

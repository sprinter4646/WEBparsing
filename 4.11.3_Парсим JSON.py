# https://stepik.org/lesson/704700/step/3?auth=login&unit=705135
# Используйте полученный по ссылке=http://parsinger.ru/downloads/get_json/res.json JSON,
# чтобы посчитать количество товара в каждой категории.
#
# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общее количество товаров
#
# Количество вы найдёте в каждой карточке товара.


import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url=url).json()
res = {'watch': 0, 'mobile': 0, 'mouse': 0, 'hdd': 0, 'headphones': 0}
for item in response:
    res.get(item["categories"])
    res[item["categories"]] += int(item["count"])
print(res)

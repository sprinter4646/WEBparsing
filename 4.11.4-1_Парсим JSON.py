# https://stepik.org/lesson/704700/step/4?auth=login&unit=705135
# Используйте полученный по ссылке=http://parsinger.ru/downloads/get_json/res.json JSON,
# чтобы посчитать стоимость товаров в каждой отдельной категории.
#
# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общая стоимость товаров.

# Павел Хошев в прошлом году
import requests

url = 'http://stepik-parsing.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
result = {}

# Считает стоимость каждой отдельной категории
for item in response:
    if item['categories'] not in result:
        result.update({item['categories']: int(item['count']) * int(item['price'].split(' ')[0])})
    else:
        result.update({item['categories']: int(result.get(item['categories'])) + (int(item['count'])
                                                                                  * int(item['price'].split(' ')[0]))})


print(result)

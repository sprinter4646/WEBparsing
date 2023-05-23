# https://stepik.org/lesson/701337/step/6?auth=login&unit=701406
# СВыберите 1 любую категорию на сайте тренажёре=http://parsinger.ru/html/index3_page_1.html,
# и соберите все данные с карточек товаров + ссылка на карточку.
#
# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.
#
# Пример:
# [
#   {
#       "categories": "watch",
#       "name": " ",
#       "article": " ",
#       "description": {
#           "brand": "",
#           "model": "",
#           "type": "",
#           "display": "",
#           "material_frame": "" ,
#           "material_bracer": "",
#           size: "",
#           site: ""
#       },
#       "count": "",
#       "price": "",
#       "old_price": "",
#       "link": ""
#   },

# Вставьте код в поле ниже и отправьте его на рецензию.


# Решение мое
# 1 выбираем категорию на сайте тренажере
# 2 формируем список ссылок для парсинга данных со страниц категории
# 3 в цикле формируем адреса страниц из выбранной категории
# 4 вкладываем цикл в котором формируем, и посещаем адреса карточек с каждой страницы из выбранной категории
# 5 на адресе карточки собираем необходимые данные, и складываем в список result_json
# 6 записываем список в файл res3.json


# импортируем нужные библиотеки
from bs4 import BeautifulSoup
import requests
import json

# 1 выбираем ссылку с категорией watch (Выберите 1 любую категорию на сайте тренажёре)
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
# 2 формируем список ссылок для парсинга данных со страниц категории
pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
# список ответа
result_json = []
# прогоняем через цикл pagen
for i in range(1, len(pagen) + 1):
    # 3 в цикле формируем адреса страниц из выбранной категории
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find('a', class_='name_item').text
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    article = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    # наполняем result_json данными из карточек
    for list_item, price_item, name in zip(description, price, name):
        result_json.append({
            'categories': 'watch',
            'name': name,
            'brand': [x.split(':')[1] for x in list_item][0],
            'type': [x.split(':')[1] for x in list_item][1],
            'connect': [x.split(':')[1] for x in list_item][2],
            'game': [x.split(':')[1] for x in list_item][3],
            'price': price_item})
# записываем и сохраняем список в файл res3.json
with open('res3.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

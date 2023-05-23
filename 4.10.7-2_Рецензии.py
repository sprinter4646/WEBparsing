# https://stepik.org/review/reviews/3370071?auth=login&unit=701406
# # Соберите данные со всех 5 категорий на сайте тренажере=http://parsinger.ru/html/index1_page_1.html
# # и соберите все данные с карточек # + ссылка на карточку с товаром.
# #
# # По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# # Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.
# #
# # Пример:
# # [
# #   {
# #       "categories": "mobile",
# #       "name": "",
# #       "article": "",
# #       "description": {
# #           "brand": "",
# #           "model": "",
# #           "material": "",
# #           "type_display": "",
# #           "diagonal": "" ,
# #           size: "",
# #           "weight": "",
# #           "resolution": "",
# #           site: ""
# #       },
# #       "count": "",
# #       "price": "",
# #       "old_price": "",
# #       "link": ""
# #   },
# #
# # Вставьте код в поле ниже и отправьте его на рецензию.


# Решение #965082890
import requests
from bs4 import BeautifulSoup
import json

cat_list = []  # Это список с названиями категорий
start_page = 'https://parsinger.ru/html/index1_page_1.html'
res = requests.get(url=start_page)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'lxml')
items = soup.find('div', {'class': 'nav_menu'}).find_all('a')
for _ in items:
    item = _.find('div')['id']
    cat_list.append(item)
json_list = []  # Будущий список словарей

for i in range(len(cat_list)):
    j = 1
    url = f'https://parsinger.ru/html/{cat_list[i]}/{i + 1}/{i + 1}_{j}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    # Название категории
    cat_name = cat_list[i]

    #  Ключи в блоке description
    keys_attr = soup.find_all('li')
    keys = []
    for _ in range(len(keys_attr)):
        keys.append(keys_attr[_]['id'])

    while response.status_code == 200:  # Что бы не определять количество страниц
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        #  Значения в блоке description
        values = []
        for _ in range(len(keys_attr)):
            values.append(keys_attr[_].text.split(':')[-1].strip())
        description = dict(zip(keys, values))

        #  Остальные значения
        name = soup.find('p', id='p_header').text.strip()
        article = soup.find('p', class_='article').text.split(':')[-1].strip()
        in_stock = soup.find('span', id='in_stock').text.split(':')[-1].strip()
        price = soup.find('span', id='price').text.strip()
        old_price = soup.find('span', id='old_price').text.strip()
        json_list.append({
            'categories': cat_name,
            'name': name,
            'article': article,
            'description': description,
            'in_stock': in_stock,
            'price': price,
            'old_price': old_price,
            'link': response.url
        })
        j += 1
        url = f'https://parsinger.ru/html/{cat_list[i]}/{i + 1}/{i + 1}_{j}.html'
        response = requests.get(url)

with open('res.json', 'w', newline='') as file:
    json.dump(json_list, file, indent=4, ensure_ascii=False)
print('Готово')

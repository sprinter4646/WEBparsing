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


# Решение #964889720
import requests
from bs4 import BeautifulSoup
import json

response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
nav_links = [link['href'] for link in soup.find('div', class_='nav_menu')('a')]
result_json = []

for nav_link in nav_links:
    response = requests.get(url=f'https://parsinger.ru/html/{nav_link}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    category = soup.find('div', class_='nav_menu').find('a', href=nav_link).find('div')['id']
    links = [link['href'] for link in soup.find('div', class_='pagen')('a')]

    for link in links:
        response = requests.get(url=f'https://parsinger.ru/html/{link}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        item_links = [item.parent['href'] for item in soup('p', string='Подробнее')]

        for item_link in item_links:
            response = requests.get(url=f'https://parsinger.ru/html/{item_link}')
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            result_json.append({
                'category': category,
                'name': soup.find('p', id='p_header').text.strip(),
                'article': soup.find('p', class_='article').text.split(':')[1].strip(),
                'description': {
                    li['id']: li.text.split(':')[1].strip() for li in soup.find('ul', id='description')('li')
                },
                'in_stock': soup.find('span', id='in_stock').text.split(':')[1].strip(),
                'price': soup.find('span', id='price').text.strip(),
                'old_price': soup.find('span', id='old_price').text.strip(),
                'link': f'https://parsinger.ru/html/{item_link}'
            })

with open('result7.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

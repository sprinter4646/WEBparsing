# https://stepik.org/review/reviews/3370071?auth=login&unit=701406
# Условие:
# Выберите 1 любую категорию на сайте тренажёре=http://parsinger.ru/html/index3_page_1.html,
# и соберите все данные с карточек товаров + ссылка на карточку.
#
# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.
#
# Пример:
# [
#   {
#       "categories": "watch",
#       "name": "Jet Kid Start blue Умные детские часы",
#       "article": "80235265",
#       "description": {
#           "brand": "Jet",
#           "model": "Excidium",
#           "type": "умные часы",
#           "display": "Монохромный",
#           "material_frame": "пластик" ,
#           "material_bracer": "силикон",
#           size: "54х34х12 мм",
#           site: "www.jetdevice.com"
#       },
#       "count": "",
#       "price": "",
#       "old_price": "",
#       "link": ""
#   },

# Вставьте код в поле ниже и отправьте его на рецензию.


# Решение #964873492
import requests
from bs4 import BeautifulSoup
import json

response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
links = [link['href'] for link in soup.find('div', class_='pagen')('a')]
result_json = []

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
            'name': soup.find('p', id='p_header').text.strip(),
            'article': soup.find('p', class_='article').text.split(':')[1].strip(),
            'description': {
                soup.find('ul', id='description')('li')[x]['id']:
                    soup.find('ul', id='description')('li')[x].text.split(':')[1].strip()
                for x in range(len(soup.find('ul', id='description')('li')))
            },
            'in_stock': soup.find('span', id='in_stock').text.split(':')[1].strip(),
            'price': soup.find('span', id='price').text.strip(),
            'old_price': soup.find('span', id='old_price').text.strip(),
            'link': f'https://parsinger.ru/html/{item_link}'
        })

with open('result.json964873492', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

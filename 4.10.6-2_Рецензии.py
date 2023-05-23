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


# Решение #959977385
import json
import requests
from bs4 import BeautifulSoup


def pars(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


cards = []
result = []
template = 'https://parsinger.ru/html/'
first_page = pars(f'{template}index1_page_1.html')
pagens = ([card['href'] for card in first_page.find('div', class_='pagen').find_all('a')])
categories = {
    'categories': (first_page.find('div', class_='nav_menu').find_next('a', {'href': 'index1_page_1.html'}).next['id'])}
for pagen in pagens:
    items = pars(f'{template}{pagen}')
    cards.extend([card.next_element['href'] for card in items.find_all('div', class_='sale_button')])
for card in cards:
    card_soup = pars(f'{template}{card}').find('div', class_='description')
    name = {'name': card_soup.find('p', id='p_header').text}
    article = {'article': card_soup.find('p', class_='article').text.split(': ', 1)[1].strip()}
    description = {'description': {x['id']: x.text.split(': ', 1)[1] for x in
                                   card_soup.find('ul', id='description').find_all('li')}}
    count = {'count': card_soup.find('span', id='in_stock').text.split(': ', 1)[1].strip()}
    price = {'price': card_soup.find('span', id='price').text}
    old_price = {'old_price': card_soup.find('span', id='old_price').text}
    link = {'link': f'{template}{card}'}
    to_result = categories | name | article | description | count | price | old_price | link
    result.append(to_result)
with open('result.json959977385', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

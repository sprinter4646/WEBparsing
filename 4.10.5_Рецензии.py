# https://stepik.org/review/reviews/3358629?auth=login&unit=701406
# Условие:
# Соберите данные со всех 5 категорий на сайте тренажере=http://parsinger.ru/html/index1_page_1.html
# и соберите все данные с карточек.
# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела
# Вставьте код в поле ниже и отправьте его на рецензию.

# Решение  # 959233358
# "Дисклеймер":
#   1. В задании не указано, что нужно собирать информацию изнутри карточек (для этого будут задания дальше,
#   как и на получение имён аттрибутов)
#   2. Поля name и price - есть у каждой позиции, аттрибутов id у этих полей нет, поэтому они указаны жестко в коде
#   3. На страницах с карточками, у <li> нет аттрибутов id, поэтому тип указан сплитом и кириллицей

import requests
from bs4 import BeautifulSoup
import json

url = 'https://parsinger.ru/html/index1_page_1.html'

# generate root url
root = url[:-len(url.split('/')[-1])]


# soup helper
def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# get links to all sections
sections = []
sections.extend(root + sections['href'] for sections in get_soup(url).find('div', class_='nav_menu').find_all('a'))

# get links to all pages
pages = []
for section_url in sections:
    pages.extend(root + page['href'] for page in get_soup(section_url).find('div', class_='pagen').find_all('a'))

# items parsing
json_data = []
for page in pages:
    soup = get_soup(page)
    for item in soup.find_all('div', class_='item'):
        item_description = [data.text for data in item.find('div', class_='description').find_all('li')]
        json_data.append({
            'Название': item.find('a', class_='name_item').text,
            item_description[0].split(':')[0].strip(): item_description[0].split(':')[1].strip(),
            item_description[1].split(':')[0].strip(): item_description[1].split(':')[1].strip(),
            item_description[2].split(':')[0].strip(): item_description[2].split(':')[1].strip(),
            item_description[3].split(':')[0].strip(): item_description[3].split(':')[1].strip(),
            'Цена': item.find('p', class_='price').text
        })

# json file output
with open('data_02.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

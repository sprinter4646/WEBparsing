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


# Решение #848179139
import json
import requests as rq
from bs4 import BeautifulSoup


def cooking_soup(link: str):
    '''For quick using "soup"'''
    response = rq.get(url=link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


res_list = []
categories = cooking_soup('https://parsinger.ru/html/index1_page_1.html').find('div', class_='nav_menu').find_all('a')
for c in categories:
    category = c.find_next('div').text
    pagen = cooking_soup(f'https://parsinger.ru/html/{c["href"]}').find('div', class_='pagen').find_all('a')
    for page in pagen:
        items = cooking_soup(f'https://parsinger.ru/html/{page["href"]}').find_all('a', class_='name_item')
        for item in items:
            url = f'https://parsinger.ru/html/{item["href"]}'
            soup_item = cooking_soup(url)
            res_list.append({'Категория': category,
                             'Название': soup_item.find('p', id='p_header').text,
                             'Артикул': soup_item.find('p', class_='article').text.split(':')[1].strip(),
                             'Описание': {i.text.split(':')[0]: i.text.split(':')[1].strip() for i in soup_item.find_all('li')},
                             'В наличии': soup_item.find('span', id='in_stock').text.split(':')[1].strip(),
                             'Цена': soup_item.find('span', id='price').text,
                             'Старая цена': soup_item.find('span', id='old_price').text,
                             'Ссылка': url})


with open('res.json', 'w', encoding='utf-8-sig', newline='') as file:
    json.dump(res_list, file, indent=4, ensure_ascii=False)

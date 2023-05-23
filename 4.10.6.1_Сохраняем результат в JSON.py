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


# Решение мое
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
# список для формирования ответа
result_json = []
# прогоняем через цикл pagen
for i in range(1, len(pagen) + 1):
    # 3 в цикле формируем номера i для адреса страниц из выбранной категории
    for j in range(1, 9):
        # 4 вкладываем цикл в котором формируем, и посещаем адреса карточек с каждой страницы из выбранной категории
        url = f'https://parsinger.ru/html/watch/1/1_{j}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        # 5 на адресе карточки собираем необходимые данные
        categories = ['watch']
        name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
        article = [x.text.strip() for x in soup.find_all('p', class_='article')]
        # ключи для словаря description
        ids = [li['id'] for li in soup.select('li[id]')]
        # значения ля словаря description
        val = soup.find('ul', id='description').find_all('li')
        # словарь description
        description = {}
        for n in range(len(ids)):
            description[ids[n]] = val[n].text[val[n].text.find(':') + 1:].strip()
        count = [x.text.strip()[x.text.find(':') + 2:] for x in soup.find_all('span', id='in_stock')]
        price = [x.text for x in soup.find('div', class_='sale').find_all('span', id='price')]
        old_price = [x.text for x in soup.find('div', class_='sale').find_all('span', id='old_price')]
        # 6 складываем собранные данные в список result_json
        for categories, name, article, count, price, old_price in zip(categories, name, article, count, price, old_price):
            result_json.append({
                'categories': categories,
                'name': name,
                'article': article,
                'description': description,
                'count': count,
                'price': price,
                'old_price': old_price,
                'link': url
            })
# 7 записываем и сохраняем список в файл res3.json
with open('res3.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

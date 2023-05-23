# https://stepik.org/lesson/701337/step/5?auth=login&unit=701406
# Соберите данные со всех 5 категорий на сайте тренажере=http://parsinger.ru/html/index1_page_1.html
# и соберите все данные с карточек.
# Решение мое
# импортируем нужные библиотеки
from bs4 import BeautifulSoup
import requests
import json

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
# Составляем список cats - ссылок на категории
cats = [f"{shema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]
# формируем список ссылок для парсинга данных со страниц категорий
pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
# список для ответа
result_json = []
# прогоняем через цикл cats
for j in range(1, len(cats) + 1):
    # прогоняем через цикл pagen
    for i in range(1, len(pagen) + 1):
        url = f'https://parsinger.ru/html/index{j}_page_{i}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]

        # наполняем result_json данными из карточек
        for list_item, price_item, name in zip(description, price, name):
            result_json.append({
                'name': name,
                'brand': [x.split(':')[1] for x in list_item][0],
                'type': [x.split(':')[1] for x in list_item][1],
                'connect': [x.split(':')[1] for x in list_item][2],
                'game': [x.split(':')[1] for x in list_item][3],
                'price': price_item})
            # сохраняем и записываем в файл res3.json
            with open('res3.json', 'w', encoding='utf-8') as file:
                json.dump(result_json, file, indent=4, ensure_ascii=False)

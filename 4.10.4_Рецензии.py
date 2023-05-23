# https://stepik.org/review/reviews/3354628?auth=login&unit=701406
# Выберите 1 любую категорию на сайте тренажере=http://parsinger.ru/html/index1_page_1.html
# и соберите все данные с карточек.
# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела
#
# Вставьте код в поле ниже и отправьте его на рецензию.
# Решение 958379643
# импортируем нужные библиотеки
from bs4 import BeautifulSoup
import requests
import json
# берем "базовый url" и делаем следующее - смотрим количество сттраниц и формируем ссылки для парсинга данных с каждой страницы
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
pagen = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
# список
result_json = []
# прогоняем через цикл
for i in range(1,len(pagen)+1):
    url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # for d in soup:
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

# ну это из лекции
    for list_item, price_item, name in zip(description, price, name):
        result_json.append({
        'name': name,
        'brand': [x.split(':')[1] for x in list_item][0],
        'type': [x.split(':')[1] for x in list_item][1],
        'connect': [x.split(':')[1] for x in list_item][2],
        'game': [x.split(':')[1] for x in list_item][3],
        'price': price_item})
# сохраняем и записываем в список
        with open('res2.json', 'w', encoding='utf-8') as file:
            json.dump(result_json, file, indent=4, ensure_ascii=False)

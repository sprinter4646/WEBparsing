# https://stepik.org/lesson/704700/step/1?auth=login&unit=705135
# Получаем ответы JSON с карточками товаров, изменяя вручную параметр в page=2
# ссылка = https://www.wildberries.ru/catalog/elektronika/planshety?sort=popular&page=2

# импортируем нужные библиотеки
from bs4 import BeautifulSoup
import requests
import json

# 1 выбираем ссылку с категорией watch (Выберите 1 любую категорию на сайте тренажёре)
url = 'https://www.wildberries.ru/catalog/elektronika/planshety?sort=popular&page=1'
schema = 'https://www.wildberries.ru/catalog/elektronika/planshety?sort=popular&page='
response = requests.get(url=url)
response.encoding = 'utf-8'
i = 1
while response.status_code == 200:
    url = f'{schema}{i}'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    print(f'sort=popular&page={i}')
    # print(soup)
    i += 1

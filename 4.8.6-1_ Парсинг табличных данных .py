# https://stepik.org/lesson/730366/step/6?unit=731870
# 1. На сайте=https://parsinger.ru/table/5/index.html расположена таблица;
# 2. Цель: Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке и всё суммировать;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')
res = []
last = [int(x.find_all('td')[-1].text) for x in soup.find_all('tr') if x.find('td')]
orange = [float(x.text) for x in soup.find_all('td', class_='orange')]

for last_item, orange_item in zip(last, orange):
    res.append(last_item * orange_item)
print(sum(res))  # >>> 2521465.6860000016

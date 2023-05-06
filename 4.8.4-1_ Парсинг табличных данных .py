# https://stepik.org/lesson/730366/step/4?unit=731870
# 1. На сайте=https://parsinger.ru/table/3/index.html расположена таблица;
# 2. Цель: Собрать числа которые выделены жирным шрифтом и суммировать их;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/3/index.html')
soup = BeautifulSoup(response.text, 'lxml')
# td = [float(x.text) for x in soup.find_all('td') if x.find('td') != x.find('b')]
td = [float(x.text) for x in soup.find_all('b')]
print(sum(td))  # >>> 373.32899999999995

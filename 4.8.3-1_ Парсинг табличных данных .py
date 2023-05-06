# https://stepik.org/lesson/730366/step/3?unit=731870
# 1. На сайте=https://parsinger.ru/table/2/index.html расположена таблица;
# 2. Цель: Собрать числа с 1го столбца и суммировать их;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/2/index.html')
soup = BeautifulSoup(response.text, 'lxml')

td = [float(x.find('td').text) for x in soup.find_all('tr') if x.find('td')]
print(sum(td))

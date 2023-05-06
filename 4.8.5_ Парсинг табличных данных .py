# https://stepik.org/lesson/730366/step/5?unit=731870
# 1. На сайте=https://parsinger.ru/table/4/index.html расположена таблица;
# 2. Цель: Собрать числа в зелёных ячейках и суммировать их;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/4/index.html')
soup = BeautifulSoup(response.text, 'lxml')
# td = [float(x.text) for x in soup.find_all('td') if x.find( class_='green')]
td = [float(x.text) for x in soup.select('td.green')]
print(sum(td))  # >>> 425.7659999999999

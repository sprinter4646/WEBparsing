# https://stepik.org/lesson/730366/step/4?unit=731870
# 1. На сайте=https://parsinger.ru/table/3/index.html расположена таблица;
# 2. Цель: Собрать числа которые выделены жирным шрифтом и суммировать их;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/3/index.html')
soup = BeautifulSoup(response.text, 'lxml')
all_cells = soup.find_all('td')  # Получаем список всех ячеек
res = 0
for x in all_cells:
    if x.find('b'):
        res += float(x.text.strip('\n'))
print(res)
# >>> 373.32899999999995

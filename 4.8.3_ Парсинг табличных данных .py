# https://stepik.org/lesson/730366/step/3?unit=731870
# 1. На сайте=https://parsinger.ru/table/2/index.html расположена таблица;
# 2. Цель: Собрать числа с 1го столбца и суммировать их;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/2/index.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
all_cells = soup.find_all('td')  # Получаем список всех ячеек
cells = [float(x.text.strip('\n')) for x in all_cells]
res = 0
for x in range(0, len(cells), 15):
    # print(cells[x])
    res += cells[x]
print(res)
#
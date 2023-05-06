# https://stepik.org/lesson/730366/step/7?unit=731870
# 1. На сайте=https://parsinger.ru/table/5/index.html расположена таблица;
# 2. Цель: Написать скрипт который формирует словарь, где ключ будет автоматически формироваться из заголовка столбцов,
# а значения это сумма всех чисел в столбце;
# 3. Округлить каждое число до 3х символов после запятой.
# 4. Полученный словарь вставить в поле ответа.
# Пример ожидаемого словаря:
# {'1 column': 000.000, '2 column': 000.000, '3 column': 000.000, '4 column': 000.000, '5 column':
# 000.00, '6 column': 000.000, '7 column': 000.000, '8 column': 000.000, '9 column': 000.000,
# '10 column': 000.000, '11 column': 000.000, '12 column': 000.000, '13 column': 000.000, '14 column':
# 000.000, '15 column': 000000.0}
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')

res = {}
row = [x.text for x in soup.find_all('th')]
for i, row in zip(range(len(row)), row):
    column = [(float(x.select('td')[i].text)) for x in soup.find_all('tr') if x.find('td')]
    res.update({
        row: round(sum(column), 3)
    })
print(res)
# >>>{'1 column': 505.206, '2 column': 369.211, '3 column': 371.566, '4 column': 659.462, '5 column': 431.64, '6 column': 426.693, '7 column': 488.112, '8 column': 487.152, '9 column': 511.983, '10 column': 403.137, '11 column': 420.792, '12 column': 468.252, '13 column': 416.635, '14 column': 443.035, '15 column': 397094.0}



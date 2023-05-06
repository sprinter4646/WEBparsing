# https://stepik.org/lesson/700231/step/6?unit=700173
# 1. Открываем сайт= http://parsinger.ru/html/index1_page_1.html
# 2. Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
# 3. Складываем все числа = 163780
# 4. Вставляем результат в поле ответа

from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find_all('p', class_="price")
print(div)
res = 0
for p in div:
    res += int(p.text.replace(' руб', ''))
print('answer =', res)

#

# https://stepik.org/lesson/700231/step/2?unit=700173
# Поиск по class, id, поиск по атрибутам
# Будем использовать наш тренажер=http://parsinger.ru/html/headphones/5/5_32.html.
#
# Поиск по id
# На этой же странице нашего тренажера есть тег <p> с id='p_header'.  Давайте посмотрим как извлекать текст по id.
from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('p', id='p_header').text
print(div)
# >>> Наушники HP Pavilion Gaming 600
# На самом деле, тут все выглядит точно так же, как и при работе с class_='', только нам нужно указать, что мы ищем id.

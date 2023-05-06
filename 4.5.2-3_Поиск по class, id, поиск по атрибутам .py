# https://stepik.org/lesson/700231/step/2?unit=700173
# Поиск по class, id, поиск по атрибутам
# Будем использовать наш тренажер=http://parsinger.ru/html/headphones/5/5_32.html.
# 
# Поиск по атрибутам
# У нас есть тег span, у которого есть атрибут name='count'. Давайте посмотрим, как извлечь текст по атрибуту.
from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('span', {'name': 'count'}).text
print(div)
# >>> В наличии: 38
# В реальных условиях поиск по атрибутам приходится использовать не очень часто,
# но важно знать, что такие возможности у нас есть, и ими не стоит пренебрегать.

# https://stepik.org/lesson/700231/step/1?unit=700173
# Навигация по структуре HTML
# Все примеры мы будем тестировать на нашем  тренажере. http://parsinger.ru/html/index1_page_1.html
#
# BeautifulSoup создает объект из HTML-дерева,
# по которому мы можем осуществлять необходимую нам навигацию и поиск элементов.
#
# Самые простые и понятные методы, которыми мы пользуемся, когда пишем наши парсеры, это:
#
# .find() - Возвращает только первый найденный элемент, узел HTML.
# .find_all() - Возвращает список элементов. Часто используется вместе с .find()
#
#
# .find()
# Давайте разбираться как работает этот метод на конкретном примере.
#
# У нас есть сайт, и мы хотим получить элемент, который имеет class='item'
from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div', 'item')
print(div.__class__)
# Здесь все очень просто: мы даем указание найти конкретный div, который имеет конкретный class='item'. Все :)
# В ответ получим <class 'bs4.element.Tag'> (print(div.__class__)), элемент класса bs4,
# с которым мы можем работать дальше.

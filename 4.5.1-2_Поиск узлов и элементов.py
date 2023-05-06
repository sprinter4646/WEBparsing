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
# .find_all()
# Давайте посмотрим на содержимое тега, который мы получили.  Видим, что мы имеем в своем распоряжении
# все те же элементы HTML. Давайте попробуем получить все теги <li>. Для этого нам понадобится метод .find_all().
from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div', 'item').find_all('li')
print(div)
# >>> [<li>Бренд: Jet</li>, <li>Тип: умные часы</li>, <li>Материал корпуса: пластик</li>,
# <li>Технология экрана: Монохромный</li>]
# Обратите внимание, что мы получили список всех элементов <li> вместе с содержимым.
# Нам бы хотелось избавиться от тегов и получить только содержимое. Метод .text к списку мы применить не можем,
# а вот пройтись по списку в цикле for и в цикле извлечь текст каждого тега это - запросто.
for txt in div:
    print(txt.text)
# >>> Бренд: Jet
# Тип: умные часы
# Материал корпуса: пластик
# Технология экрана: Монохромный
# p.s. Чтобы не городить цикл в две строки, мы можем воспользоваться list comprehension:
div = [x.text for x in soup.find('div', 'item').find_all('li')]
print(*div, sep='\n')

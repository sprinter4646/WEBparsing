# https://stepik.org/lesson/896231/step/2?unit=901222
# soup.find_all() - это метод Beautiful Soup, который ищет все элементы в HTML-документе, соответствующие переданным
# параметрам. Возвращает список элементов Beautiful Soup, которые удовлетворяют условиям поиска.
#
# soup.find_all(self, name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)
# Параметры:
#
# name - имя тега HTML, который нужно найти. Опциональный параметр.
# attrs - словарь атрибутов и их значений, которые нужно найти. Опциональный параметр.
# text - текст, который нужно найти. Опциональный параметр.
# limit - максимальное количество элементов, которые мы хотим найти. Опциональный параметр.
# recursive - определяет, должны ли мы искать элементы во вложенных тегах. По умолчанию True. Опциональный параметр.
# Пример 5
#
# С помощью метода find_all() ищутся все теги p с указанными атрибутами class или id. Найденные теги циклом
# перебираются, а текст каждого тега выводится в консоль.
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p` с классом `text-class`
result = soup.find_all('p', {'class': 'text-class'})
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `class`
result = soup.find_all('p', class_=True)
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `id`
result = soup.find_all('p', id=True)
for tag in result:
    print(tag.text)

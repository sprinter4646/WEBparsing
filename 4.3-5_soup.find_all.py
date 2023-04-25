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
# Пример 3 с применением recursive=True
#
# Код ищет все теги 'p' в HTML-документе, включая те, что находятся внутри вложенных тегов, используя метод find_all()
# с параметром recursive=True. Наконец, эти теги выводятся в консоль.
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найти все теги p в HTML-документе, включая те, что находятся внутри вложенных тегов.
all_p_tags = soup.find_all('p', recursive=True)
print(all_p_tags)

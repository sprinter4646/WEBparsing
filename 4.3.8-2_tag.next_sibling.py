# https://stepik.org/lesson/896231/step/8?unit=901222
# tag.next_sibling - это метод BeautifulSoup, который возвращает следующий элемент, следующий за текущим элементом.
# Он возвращает следующий элемент, независимо от того, является ли он тегом, текстом или пробелами.
#
# Пример 2
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Example Page</h1>
        <p>This is some text.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
        <p>This is some more text.</p>
        <p>This is even more text.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

first_para = soup.p
print(first_para)
print(first_para.next_sibling)
# Вывод:
# <p>This is some text.</p>

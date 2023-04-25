# https://stepik.org/lesson/896231/step/8?unit=901222
# tag.next_sibling - это метод BeautifulSoup, который возвращает следующий элемент, следующий за текущим элементом.
# Он возвращает следующий элемент, независимо от того, является ли он тегом, текстом или пробелами.
#
# Пример 1
#
# Таким образом, мы можем использовать метод .next_sibling для перехода к следующему элементу в документе.
# Это полезно, когда мы хотим пройти по всему документу и извлечь необходимую информацию.
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
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

header = soup.h1
print(header)
print(header.next_sibling)
# Вывод:
# <h1>Example Page</h1>

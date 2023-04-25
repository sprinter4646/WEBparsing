# https://stepik.org/lesson/896231/step/3?unit=901222
# tag.text - это свойство BeautifulSoup-объекта, которое возвращает текстовое содержимое тега, включая текст,
# содержащийся между тегами. Оно не учитывает вложенные теги.
# .text
# Пример 1
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div id="main">
            <p>This is a paragraph</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим первый элемент с тегом p
p = soup.find('p')

# Используем .text, чтобы получить текст внутри тега p
print(p.text)  # This is a paragraph
# Вывод:
# This is a paragraph

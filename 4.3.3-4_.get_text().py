# https://stepik.org/lesson/896231/step/3?unit=901222
# .get_text()  - это метод BeautifulSoup-объекта, который возвращает текстовое содержимое тега и всех его потомков
# (включая текст, содержащийся между вложенными тегами). Он может быть использован для извлечения всего текстового
# содержимого внутри тега.
# .get_text()
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

all_text = soup.get_text()
print(all_text)
# Вывод:
# Example Page
# This is some text.
#
# Item 1
# Item 2
# Item 3
#
# This is some more text.
# This is even more text.

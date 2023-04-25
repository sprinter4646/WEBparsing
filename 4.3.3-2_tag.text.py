# https://stepik.org/lesson/896231/step/3?unit=901222
# tag.text - это свойство BeautifulSoup-объекта, которое возвращает текстовое содержимое тега, включая текст,
# содержащийся между тегами. Оно не учитывает вложенные теги.
# .text
# Пример 2
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div id="main">
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим все теги li
lis = soup.find_all('li')

# Выводим текст внутри каждого тега li с помощью .text
for li in lis:
    print(li.text)
# Вывод:
# Item 1
# Item 2
# Item 3

# https://stepik.org/lesson/896231/step/6?unit=901222
# tag.parent - это свойство объекта Beautiful Soup, которое возвращает родительский тег текущего элемента.
#
# Пример 3
#
# Ищем все элементы <b> в HTML-документе и выводим текст их родительского элемента:
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <p>This is a <b>bold</b> text.</p>
        <p>This is another <b>bold</b> text.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")
bold_elements = soup.find_all("b")

for b in bold_elements:
    print(b.parent.text)
# Вывод:
# This is a bold text.
# This is another bold text.

# https://stepik.org/lesson/896231/step/6?unit=901222
# tag.parent - это свойство объекта Beautiful Soup, которое возвращает родительский тег текущего элемента.
#
# Пример 2
#
# В этом примере мы ищем тег p с помощью метода find() и получаем его родительский тег с помощью атрибута parent.
# Результатом будет тег body.
from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <p>This is a paragraph.</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
p_tag = soup.find('p')
body_tag = p_tag.parent
print(body_tag)
# Вывод:
# body

# https://stepik.org/lesson/896231/step/6?unit=901222
# tag.parent - это свойство объекта Beautiful Soup, которое возвращает родительский тег текущего элемента.
#
# Пример 1
#
# В приведенном примере p_element - это объект BeautifulSoup, соответствующий тегу p, и parent
# - это родительский элемент тега p, то есть тег body.
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p>This is a paragraph.</p>
  </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
p_element = soup.find("p")
parent = p_element.parent
print(parent.name)  # body
# Вывод:
# body

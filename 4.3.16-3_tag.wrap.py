# https://stepik.org/lesson/896231/step/16?unit=901222
# tag.wrap - метод в BeautifulSoup служит для обертывания тегов в документе HTML.
# Он принимает в качестве параметра любой объект BeautifulSoup, и возвращает новый объект BeautifulSoup,
# содержащий исходный объект в качестве дочернего элемента.
#
# Пример 1
from bs4 import BeautifulSoup

html_doc = """
<body>
  <p>Some text</p>
</body>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Обернем первый тег p внутри body с помощью тега div
p_tag = soup.body.p
p_tag.wrap(soup.new_tag("div", class_='wrap_tag'))

print(soup)
# Вывод:
# <body>
# <div class_="wrap_tag"><p>Some text</p></div>
# </body>

# https://stepik.org/lesson/896231/step/7?unit=901222
# tag.children - представляет собой объект ResultSet, который содержит все дочерние элементы тега.
# Он позволяет легко проходиться по всем дочерним элементам и выполнять операции с ними.
# Например, можно использовать цикл for, чтобы проходиться по всем дочерним элементам и выполнять различные операции
# с каждым из них. Например, можно выбрать все ссылки внутри тега,
# используя метод find_all() для каждого дочернего элемента.
#
# Пример 1
#
# Используем .children для перебора всех дочерних элементов тега <div class="content">:
from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <div class="content">
      <p>This is some content.</p>
      <p>This is some more content.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

content = soup.find('div', {'class': 'content'})

for child in content.children:
    print(child)
# Вывод:
# <p>This is some content.</p>
# <p>This is some more content.</p>

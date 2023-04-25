# https://stepik.org/lesson/896231/step/7?unit=901222
# tag.children - представляет собой объект ResultSet, который содержит все дочерние элементы тега.
# Он позволяет легко проходиться по всем дочерним элементам и выполнять операции с ними.
# Например, можно использовать цикл for, чтобы проходиться по всем дочерним элементам и выполнять различные операции
# с каждым из них. Например, можно выбрать все ссылки внутри тега,
# используя метод find_all() для каждого дочернего элемента.
#
# Пример 2
from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <div class="container">
      <h1>Welcome to our website!</h1>
      <p>This is some text.</p>
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

container = soup.find('div', {'class': 'container'})

for child in container.children:
    print(child)
# Вывод:
# <h1>Welcome to our website!</h1>
# <p>This is some text.</p>
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>
# </ul>

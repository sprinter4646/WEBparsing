# https://stepik.org/lesson/896231/step/13?unit=901222
# tag.extract() - это метод объекта BeautifulSoup, который используется для извлечения тега из дерева документа.
# Когда тег извлекается, он не доступен для дальнейшей обработки или поиска. Он полностью удаляется из документа.
#
# Пример 1
#
# В результате выполнения кода, тег h1 будет исключен из документа.
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найдёт первый div с идентификатором "main"
main_div = soup.find('div', {'id': 'main'})

# Найдёт первый h1 внутри "основного" div
main_h1 = main_div.find('h1')

# Извлекает тег h1 из документа
main_h1.extract()

# Тег h1 больше не доступен в документе
print(soup)
# Вывод:
# <html>
# <head>
# <title>Example Page</title>
# </head>
# <body>
# <div id="main">
#
# <p class="info">This is a paragraph.</p>
# <p class="info">This is another paragraph.</p>
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>
# </ul>
# </div>
# <div id="secondary">
# <p>Some additional information.</p>
# </div>
# </body>
# </html>

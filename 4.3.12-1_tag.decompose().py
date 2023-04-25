# https://stepik.org/lesson/896231/step/12?unit=901222
# tag.decompose() - это метод Beautiful Soup, который удаляет тег и все его дочерние элементы из дерева документа.
# Он используется, если вы хотите удалить какой-либо элемент из парсированного документа.
#
# Пример 1
#
# В этом примере первый тег <p class="info"> внутри <div id="main"> удаляется с помощью метода .decompose().
# Вывод main_div после вызова .decompose() не будет включать первый тег <p class="info">.
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

# Найдёт первый div с идентификатором «main»
main_div = soup.find('div', {'id': 'main'})

# Найдёт первый тег p с классом «info» внутри «main» div и удалит его.
info_p = main_div.find('p', {'class': 'info'})
info_p.decompose()
print(main_div)
# Вывод:
# <div id="main">
# <h1>Hello World</h1>
#
# <p class="info">This is another paragraph.</p>
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>
# </ul>
# </div>

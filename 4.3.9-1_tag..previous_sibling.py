# https://stepik.org/lesson/896231/step/9?unit=901222
# tag..previous_sibling - это метод для получения предыдущего элемента в одном уровне вложенности (т.е. sibling)
# относительно текущего элемента.
#
# Как и в случае с .next_sibling, если текущий элемент является первым элементом в уровне вложенности,
# то previous_sibling вернет None.
#
# Пример 1
#
# Код ищет последний элемент списка <li> в HTML-документе и выводит его. Затем используется метод .previous_sibling
# для получения предыдущего соседнего элемента. Код продолжает искать предыдущие соседние элементы до тех пор,
# пока не найдет элемент.
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

last_list_item = soup.find_all('li')[-1]

previous_sibling = last_list_item.previous_sibling
while previous_sibling:
    print(previous_sibling)
    previous_sibling = previous_sibling.previous_sibling
# Вывод:
# <li>Item 2</li>
#
# <li>Item 1</li>

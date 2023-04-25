# https://stepik.org/lesson/896231/step/6?unit=901222
# tag.parent - это свойство объекта Beautiful Soup, которое возвращает родительский тег текущего элемента.
#
# Пример 4
#
# Используем метод .select_one для выбора первого тега <p>, который является дочерним элементом тега <div id="content">.
# Затем родитель выбранного тега сохраняется в переменной parent_div, которая, наконец, выводится на печать.
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <div id="content">
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

first_p = soup.select_one('#content p:first-of-type')
parent_div = first_p.parent

print(parent_div)
# Вывод:
# <div id="content">
# <p>This is a paragraph.</p>
# <p>This is another paragraph.</p>
# </div>

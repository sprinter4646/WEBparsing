# https://stepik.org/lesson/896231/step/5?unit=901222
# .select_one()
# soup.select_one() - это метод Beautiful Soup, который позволяет выбрать один элемент на основе CSS-селектора.
# Он возвращает первый найденный элемент, удовлетворяющий условию, или None, если ничего не было найдено.
# Этот метод полезен, когда вы знаете, что только один элемент должен удовлетворять условию.
#
# .select_one() принимает тот же аргумент, что и .select(), т.е. CSS selector. Разница между ними в том,
# что .select_one() возвращает только первый найденный тег,
# в то время как .select() возвращает список всех найденных тегов.
#
# select_one(self, selector, namespaces=None, **kwargs)
# Пример 3
#
# Используем метод "select_one", который выбирает первый элемент с селектором ".container p.highlight",
# т.е. первый элемент тега p с классом "highlight" внутри первого элемента тега div с классом "container".
# Наконец, выбранный элемент выводится на консоль.
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <div class="container">
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </div>
        <div class="container">
            <p class="highlight">This is a highlighted paragraph.</p>
            <p>This is a fourth paragraph.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Выберем первый div с классом «container», у которого есть дочерний элемент p с классом «highlight».
highlighted_paragraph = soup.select_one('.container p.highlight')
print(highlighted_paragraph)
# Вывод:
# <p class="highlight">This is a highlighted paragraph.</p>

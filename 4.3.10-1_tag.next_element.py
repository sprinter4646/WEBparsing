# https://stepik.org/lesson/896231/step/10?unit=901222
# tag.next_element - это метод Beautiful Soup, который возвращает следующий элемент в документе HTML,
# следуя порядку их вхождения. Этот метод полезен для перемещения по документу HTML последовательно,
# пропуская все пробелы, теги и другие ненужные элементы. Таким образом, .next_element позволяет получить следующий
# элемент в документе HTML. Если следующий элемент отсутствует, метод возвращает None.
#
# Пример 1
#
# Код использует метод .li для получения первого элемента списка <li> в HTML-документе.
# Далее, используется метод .next_element для получения следующего элемента в HTML-документе.
# Затем, в цикле while, выводится каждый следующий элемент, пока не достигнут конец HTML-документа.
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

first_p = soup.li
print(first_p)

next_element = first_p.next_element
while next_element:
    print(next_element)
    next_element = next_element.next_element
# Вывод:
# <li>Item 1</li>
# Item 1
#
# <li>Item 2</li>
# Item 2
#
# <li>Item 3</li>
# Item 3
#
# <p>This is some more text.</p>
# This is some more text.
#
# <p>This is even more text.</p>
# This is even more text.


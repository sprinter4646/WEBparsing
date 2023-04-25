# https://stepik.org/lesson/896231/step/11?unit=901222
# tag.previous_element - это метод BeautifulSoup, который возвращает предыдущий элемент в разметке HTML.
# Он является аналогом метода .next_element, но работает в обратном направлении, т.е. возвращает предыдущий элемент,
# расположенный до текущего. Если предыдущий элемент отсутствует, метод возвращает None.
#
# Пример 1
#
# В этом примере мы находим последний элемент <p> в разметке HTML и используем метод .previous_element,
# чтобы получить предыдущий элемент. Затем мы продолжаем использовать этот метод,
# чтобы получить другой предыдущий элемент.
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

last_p = soup.find_all('li')[-1]

previous_element = last_p.previous_element

previous_element = previous_element.previous_element
print(previous_element)
# Вывод:
# Item 2

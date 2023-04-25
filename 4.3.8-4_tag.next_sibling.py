# https://stepik.org/lesson/896231/step/8?unit=901222
# tag.next_sibling - это метод BeautifulSoup, который возвращает следующий элемент, следующий за текущим элементом.
# Он возвращает следующий элемент, независимо от того, является ли он тегом, текстом или пробелами.
#
# Пример 4
#
# Этот код парсит HTML-документ с помощью библиотеки BeautifulSoup и выводит текст всех элементов li после первого
# элемента li в списке ul.
#
# С помощью метода soup.li получаем первый элемент li в документе.
# С помощью метода next_sibling получаем следующий элемент после первого li.
# В цикле while проверяем, является ли следующий элемент li. Если да, то выводим текст этого элемента. Если нет,
# то продолжаем итерацию.
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

first_list_item = soup.li
print(first_list_item.text)

print('----разделитель----')

next_sibling = first_list_item.next_sibling
while next_sibling:
    if next_sibling.name == 'li':
        print(next_sibling.text)
    next_sibling = next_sibling.next_sibling
# Вывод:
# Item 1
# ----разделитель----
# Item 2
# Item 3

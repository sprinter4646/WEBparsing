# https://stepik.org/lesson/896231/step/9?unit=901222
# tag..previous_sibling - это метод для получения предыдущего элемента в одном уровне вложенности (т.е. sibling)
# относительно текущего элемента.
#
# Как и в случае с .next_sibling, если текущий элемент является первым элементом в уровне вложенности,
# то previous_sibling вернет None.
#
# Пример 2
#
# Код находит последний элемент p в HTML с помощью метода find_all() и индекса [-1].
# Затем он использует метод .previous_sibling для получения предыдущего соседа элемента p.
# Это повторяется дважды, пока не достигнется предыдущий сосед.
# В итоге код выводит предыдущий элемент перед последним элементом p, которым является список ul.
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

last_p = soup.find_all('p')[-1]

prev_sibling = last_p.previous_sibling

print(prev_sibling.previous_sibling)
# Вывод:
# <p>This is some more text.</p>
# В этом коде дважды применяется .previous_sibling.previous_sibling для того, чтобы пропустить текстовые узлы между
# тегами и получить предыдущий соседний тег. В данном случае, это нужно для поиска предыдущего тега <p>
# относительно последнего тега <p> в HTML-структуре.
#
# Вот что происходит:
#
# Используя last_p = soup.find_all('p')[-1], находится последний тег <p> в HTML-структуре:
# <p>This is even more text.</p>.
# last_p.previous_sibling вернет символы новой строки и пробелы между последним и предпоследним тегами <p>,
# которые представляют собой текстовый узел.
# Чтобы получить предыдущий тег <p>, нужно ещё раз вызвать .previous_sibling. Таким образом,
# last_p.previous_sibling.previous_sibling вернет предпоследний тег <p>: <p>This is some more text.</p>.


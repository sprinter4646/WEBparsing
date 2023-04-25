# https://stepik.org/lesson/896231/step/4?unit=901222
# soup.select() - это метод Beautiful Soup, который позволяет выполнять поиск элементов HTML с помощью CSS селекторов.
# Он возвращает список тегов, удовлетворяющих заданным условиям.
#
# Вы можете использовать CSS селекторы, такие как тег, класс, идентификатор и другие атрибуты, чтобы найти нужные
# элементы в документе HTML. Например, вы можете использовать селектор p.text-class, чтобы найти все теги p с классом
# text-class. Или вы можете использовать селектор p#text-id, чтобы найти тег p с идентификатором text-id.
#
# Обратите внимание, что select() всегда возвращает список тегов, даже если вы ищете один тег. Чтобы получить один тег,
# вы можете использовать индекс [0] или метод select_one().
#
# soup.select(self, selector, namespaces=None, limit=None, **kwargs)
# Параметры:
#
# Тег: select("p")
# Класс: select(".class")
# Идентификатор: select("#id")
# Атрибут: select("[attribute=value]")
# Несколько селекторов: select("p.class")
# Пример 1
#
# Используем метод .select() у объекта soup, который позволяет выбрать теги с определенными селекторами.
# В первом случае выбираются все теги p с классом text-class, во втором - теги p с атрибутом id, а в третьем - все
# теги p внутри тега body. В результате текст этих тегов выводится на экран.
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p` с классом `text-class`
result = soup.select('p.text-class')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом `id`
result = soup.select('p#text-id')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` внутри тега `body`
result = soup.select('body p')
for tag in result:
    print(tag.text)
# Вывод:
# Текст 1
# Текст 2
# ----разделитель - ---
# Текст 3
# ----разделитель - ---
# Текст 1
# Текст 2
# Текст 3


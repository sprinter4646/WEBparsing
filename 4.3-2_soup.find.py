# https://stepik.org/lesson/896231/step/2?unit=901222
# soup.find() - это метод, который ищет первый элемент, удовлетворяющий заданным критериям, в дереве элементов
# Beautiful Soup. Если такой элемент не найден, возвращается None.
#
# soup.find(name, attrs, recursive, string, **kwargs)
# Параметры:
#
# name - имя тега элемента, который вы хотите найти. Это может быть строкой или регулярным выражением.
# attrs - словарь атрибутов элемента, которые вы хотите найти.
# recursive - если установлено в False, метод ищет только в первых дочерних элементах, иначе поиск происходит во всех
# подэлементах. По умолчанию равен True.
# string - строка, которую вы хотите найти.
# Пример 3 с применением attrs
#
# Код ищет первый div с идентификатором "main" и первый тег p с классом "info" в объекте "soup" и выводит результаты.
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

# Найдите первый div с идентификатором «main»
main_div = soup.find('div', attrs={'id': 'main'})
print(main_div)

print('----разделитель----')

# Найдите первый тег p с классом "info"
info_p = soup.find('p', attrs={'class': 'info'})
print(info_p)

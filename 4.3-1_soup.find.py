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
# Пример 2
# Используем метод find() для нахождения первого div с атрибутом id='main'. Далее внутри этого div используется
# метод find() для поиска первых тегов h1, p с классом 'info' и ul. Найденные теги выводятся в консоль.
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

# Находим первый div с id "main"
main_div = soup.find('div', {'id': 'main'})
print(main_div)

print('----разделитель----')

# Найдите первый тег h1 внутри «основного» div
main_h1 = main_div.find('h1')
print(main_h1)

print('----разделитель----')

# Найдите первый тег p с классом «информация» внутри «основного» div
main_p = main_div.find('p', {'class': 'info'})
print(main_p)

print('----разделитель----')

# Найдите первый тег ul внутри «основного» div
main_ul = main_div.find('ul')
print(main_ul)

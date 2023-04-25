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
# Пример 1
# Код ищет первый тег h1 и первый тег p с классом "info", и выводит их на экран.
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <p class="info">This is a paragraph.</p>
        <p class="info">This is another paragraph.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найдёт первый тег h1
first_h1 = soup.find('h1')
print(first_h1)

print('----разделитель----')

# Найдёт первый тег p с классом "info"
first_p = soup.find('p', {'class': 'info'})
print(first_p)

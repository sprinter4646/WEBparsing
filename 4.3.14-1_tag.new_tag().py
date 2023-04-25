# https://stepik.org/lesson/896231/step/14?unit=901222
# soup.new_tag() - это метод в BeautifulSoup, который используется для создания нового тега.
# Он принимает имя тега в качестве аргумента и возвращает новый экземпляр тега,
# который может быть добавлен в дерево документа.
#
# new_tag(self, name, namespace=None, nsprefix=None, attrs={}, sourceline=None, sourcepos=None, **kwattrs)
# "name" - имя создаваемого тега.
# "namespace" - пространство имен, которое может использоваться тегом.
# "nsprefix" - префикс, используемый для идентификации пространства имен.
# "attrs" - словарь атрибутов тега, например {"class": "example", "id": "example-id"}.
# "sourceline" - номер строки в HTML-документе, где тег был создан.
# "sourcepos" - позиция тега в HTML-документе.
# "kwattrs" - дополнительные атрибуты, переданные в виде ключевых аргументов.
# Пример 1
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <p>Hello World!</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Создадим новый тег h1
new_h1 = soup.new_tag("h1", class_='new_class_tag')

# Добавим текст в новый тег h1
new_h1.string = "Welcome"

# Вставим новый тег h1 в документ
soup.body.insert(0, new_h1)

print(soup)
# Вывод:
# <html>
# <body><h1 class_="new_class_tag">Welcome</h1>
# <p>Hello World!</p>
# </body>
# </html>

# https://stepik.org/lesson/896231/step/15?unit=901222
# .insert_after()
# .insert_before()
# .insert()
# tag.insert_after(new_tag) - этот метод используется для вставки дочернего элемента
# после текущего элемента в BeautifulSoup.
#
# tag.insert_before(new_tag) - метод используется для вставки тега (Tag) перед другим тегом.
# Метод принимает в качестве аргумента тег, который необходимо вставить. После вызова .insert_before() тег,
# который был передан в качестве аргумента, становится предыдущим элементом относительно текущего тега.
#
# tag.insert(0, new_tag) - это метод BeautifulSoup, который позволяет вставить другой элемент структуры HTML
# внутрь элемента, к которому применяется метод. Метод принимает два параметра:
#
# index: индекс, по которому новый элемент будет вставлен
# element: элемент, который необходимо вставить внутрь элемента
# Все три метода принимают два аргумента: элемент, который нужно вставить (поддерево);
#
#  Пример .insert_after()
# В этом примере мы создаем новый тег b с текстом "Important" и вставляем его после первого p тега.
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <p>Paragraph 1</p>
        <p>Paragraph 2</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Создаём тег который будем добавлять
new_tag = soup.new_tag("b", id='insert_after_tag')
new_tag.string = "Important"

first_p = soup.find("p")
first_p.insert_after(new_tag)

print(soup)
# Вывод:
# <html>
# <body>
# <p>Paragraph 1</p><b id="insert_after_tag">Important</b>
# <p>Paragraph 2</p>
# </body>
# </html>

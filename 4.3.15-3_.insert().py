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
#  Пример .insert()
# Находим первый тег ul внутри div с id="main". Затем создается новый тег li с текстом "Item 4 insert_index".
# Новый тег li добавляется в тег ul с индексом 0 (то есть станет первым элементом списка). В конце выводится тег ul.
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div id="main">
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим первый div с id "main"
main_div = soup.find('ul')

# Создаёт тег li
new_li = soup.new_tag("li")
# Устанавливает текст внутри созданного li
new_li.string = "Item 4 insert_index"

# Добавляем созданный тег li в тег ul на индекс 0
main_div.insert(7, new_li)

print(main_div)
# Вывод с .insert(0, new_li):
#
# <ul>   <li>Item 4 insert_index</li>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>
# </ul>
#
#
# Вывод с .insert(1, new_li):
#
# <ul>
# <li>Item 4 insert_index</li>   <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>
# </ul>
#
#
# Вывод с .insert(2, new_li):
#
# <ul>
# <li>Item 1</li>   <li>Item 4 insert_index</li>
# <li>Item 2</li>
# <li>Item 3</li>
# </ul>
#
#
# Вывод с .insert(3, new_li):
#
# <ul>
# <li>Item 1</li>
# <li>Item 4 insert_index</li>   <li>Item 2</li>
# <li>Item 3</li>
# </ul>
#
#
# Вывод с .insert(4, new_li):
#
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>    <li>Item 4 insert_index</li>
# <li>Item 3</li>
# </ul>
#
#
# Вывод с .insert(5, new_li):
#
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 4 insert_index</li>   <li>Item 3</li>
# </ul>
#
#
# Вывод с .insert(6, new_li):
#
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>   <li>Item 4 insert_index</li>
# </ul>
#
#
# Вывод с .insert(7, new_li):
#
# <ul>
# <li>Item 1</li>
# <li>Item 2</li>
# <li>Item 3</li>
# <li>Item 4 insert_index</li>   </ul>

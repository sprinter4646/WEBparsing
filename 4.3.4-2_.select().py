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
# Пример 2
#
# Использует метод select для выбора всех параграфов с классом "highlight" и выводит текст этих параграфов.
# Также он выбирает все параграфы, находящиеся внутри элемента с идентификатором "div1",
# и выводит текст этих параграфов.
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <p class="highlight">This is a highlighted paragraph.</p>
    <p>This is a normal paragraph.</p>
    <div id="div1">
      <p>This is a paragraph in a div.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight"
highlighted_paras = soup.select(".highlight")
for para in highlighted_paras:
    print(para.text)

print('----разделитель----')

# Выберем все параграфы, находящиеся внутри элемента с идентификатором "div1"
div_paras = soup.select("#div1 p")
for para in div_paras:
    print(para.text)
# Вывод:
# This is a highlighted paragraph.
# ----разделитель----
# This is a paragraph in a div.


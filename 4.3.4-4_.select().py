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
# Пример 4
#
# Используем метод "select" для выбора всех параграфов с классом "highlight". Наконец, он выводит текст этих параграфов.
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <div id="div1">
      <p class="highlight">This is a highlighted paragraph in div1.</p>
      <p>This is a normal paragraph in div1.</p>
    </div>
    <div id="div2">
      <p class="highlight">This is a highlighted paragraph in div2.</p>
      <p>This is a normal paragraph in div2.</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Выберем все параграфы с классом "highlight"
highlighted_paras = soup.select("p[class='highlight']")
print("Highlighted paragraphs:")
for para in highlighted_paras:
    print(para.text)
# Вывод:
# Highlighted paragraphs:
# This is a highlighted paragraph in div1.
# This is a highlighted paragraph in div2.

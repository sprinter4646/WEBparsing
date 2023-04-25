# https://stepik.org/lesson/896231/step/5?unit=901222
# .select_one()
# soup.select_one() - это метод Beautiful Soup, который позволяет выбрать один элемент на основе CSS-селектора.
# Он возвращает первый найденный элемент, удовлетворяющий условию, или None, если ничего не было найдено.
# Этот метод полезен, когда вы знаете, что только один элемент должен удовлетворять условию.
#
# .select_one() принимает тот же аргумент, что и .select(), т.е. CSS selector. Разница между ними в том,
# что .select_one() возвращает только первый найденный тег,
# в то время как .select() возвращает список всех найденных тегов.
#
# select_one(self, selector, namespaces=None, **kwargs)
# Пример 1
#
# Код использует метод select_one для выбора первого тега p с атрибутом «class», равным «highlight».
# Затем текст выбранного тега извлекается и печатается.
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

# Выберем первый параграф с классом "highlight"
highlighted_para = soup.select_one("p[class='highlight']")
print("Highlighted paragraph:")
print(highlighted_para.text)
# Вывод:
# Highlighted paragraph:
# This is a highlighted paragraph in div1.

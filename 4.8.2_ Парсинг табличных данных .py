# https://stepik.org/lesson/730366/step/2?unit=731870
# 1. На сайте=https://parsinger.ru/table/1/index.html расположена таблица;
# 2. Цель: собрать все уникальные числа из таблицы (кроме цифр в заголовке) и суммировать их;
# 3. Полученный результат вставить в поле ответа.
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
all_cells = soup.find_all('td')  # Получаем список всех ячеек
cells = {float(x.text.strip('\n')) for x in all_cells}
print(sum(cells))
res = 0
for x in cells:
    res += x
print(res)
# >>> 1240.0959999999998
# Для начала нам нужно понять, как устроены таблицы в HTML. Любая таблица состоит из табличных тегов,
# перечисленных ниже:
#
# <table> </table> - служит основным тегом контейнеров для ячеек таблицы, любая таблица начинается с этого тега;
# <td></td> - (table data) создает ячейку, в которой могут хранится любые данные;
# <th></th> - (table header) создает ячейку-заголовок для столбца в таблице;
# <tr></tr> - (table row) создает строку в таблице, любая таблица должна иметь хотя бы 1 строку.
# Пример таблицы с простыми ячейками <td></td>
#
#
#
# <table>
#     <tr>
#       <td><b>td</b> - Ячейка 1</td>
#       <td><b>td</b> - Ячейка 2</td>
#     </tr>
#     <tr>
#       <td><b>td</b> - Ячейка 3</td>
#       <td><b>td</b> - Ячейка 4</td>
#     </tr>
# </table>
#
#
# Пример таблицы с заголовками <th></th>
#
#
#
# <table>
#    <tr>
# 	 <th>th - Заголовок</th>
# 	 <th>th - Заголовок</th>
#    </tr>
#    <tr>
# 	 <td><b>td</b> - Ячейка 1</td>
# 	 <td><b>td</b> - Ячейка 2</td>
#    </tr>
#    <tr>
# 	 <td><b>td</b> - Ячейка 3</td>
# 	 <td><b>td</b> - Ячейка 4</td>
#    </tr>
# </table>

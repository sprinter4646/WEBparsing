# https://stepik.org/lesson/730366/step/1?unit=731870
# Парсинг табличных данных
# Парсинг табличных данных ничем не отличается от парсинга других данных, за исключением того, что данные лежат в
# таблице. Если вы собираетесь заниматься обработкой больших данных, то парсингом таблиц вы будете заниматься регулярно.
#
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

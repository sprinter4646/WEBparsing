# https://stepik.org/lesson/700334/step/2?unit=700275
# Пагинация часть -2
# Подобным образом мы получим сразу 100 готовых для парсинга ссылок. Загвоздка заключается в том, что мы заранее не
# знаем, сколько на странице ссылок в пагинации. А вдруг завтра количество страниц может быть увеличено или уменьшено,
# и наш парсер либо упадет с ошибкой, либо не дотянется до новых страниц?
#
# Поэтому нам нужно извлечь последнее значение из пагинации перед генерацией ссылок.
#
# За основу примера возьмём наш тренажер = http://parsinger.ru/html/index1_page_1.html.
from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

print(pagen)

# >>> 4
# Мы применили индексацию [-1],
# чтобы получить последний элемент списка, в котором хранился весь список значений пагинации.

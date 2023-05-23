# https://stepik.org/lesson/701337/step/3?auth=login&unit=701406
# JSON часть 3
# В этой части мы поговорим о том, как извлекать значения атрибута. Именно его значение, а не текст, который заключен
# в теге. Этим методом можно собирать любые значения атрибутов, class="", name="", src="", href="", id="",
# не имеет значения какой тег. Чтоб далеко не ходить, мы будем тренироваться на нашем
# тренажёре = http://parsinger.ru/html/watch/1/1_1.html
# <ul id="description">
# <li id="brand">...</li>
# <li id="model">...</li>
# <li id="type">...</li>
# <li id="display">...</li>
# <li id="material_frame">...</li>
# <li id="material_bracer">...</li>
# <li id="size">...</li>
# <li id="site">...</li>
# </ul>
# В результате выполнения кода у нас получится вот такой список:
# ['brand', 'model', 'type', 'display', 'material_frame', 'material_bracer', 'size', 'site'].
# Это понадобится вам для решения задачи, которая ждет вас далее.
import requests
from bs4 import BeautifulSoup

response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')

for li in description:
    print(li['id'])


# >>>
    # brand
    # model
    # type
    # display
    # material_frame
    # material_bracer
    # size
    # site

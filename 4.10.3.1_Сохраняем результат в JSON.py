# https://stepik.org/lesson/701337/step/3?auth=login&unit=701406
# JSON часть 3
# В первую очередь нам необходимо найти и получить родительский элемент, в этом примере это <ul id="description">,
# description = soup.find('ul', id='description').find_all('li') - будет хранить список всех дочерних элементов <li>,
# давайте на них посмотрим.
# <li id="brand">Бренд: Jet</li>
# <li id="model">Модель: Excidium</li>
# <li id="type">Тип подключения: умные часы</li>
# <li id="display">Технология экрана: Монохромный</li>
# <li id="material_frame">Материал корпуса: пластик</li>
# <li id="material_bracer">Материал браслета: силикон</li>
# <li id="size">Размеры: 54х34х12 мм</li>
# <li id="site">Сайт производителя: www.jetdevice.com</li>
# Далее мы проходимся по каждому элементу в этом списке и обращаемся с ним как с элементами словаря - li['id'].
# Мы можем добавлять элементы в список на каждой итерации, а можем использовать list comprehension
# li_id = [x['id'] for x in description] и получить готовый список без лишнего кода.
import requests
from bs4 import BeautifulSoup

response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')
li_id = [x['id'] for x in description]
print(li_id)


# >>> ['brand', 'model', 'type', 'display', 'material_frame', 'material_bracer', 'size', 'site']

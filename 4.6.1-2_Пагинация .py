# https://stepik.org/lesson/700334/step/1?unit=700275
# Пагинация
#
# Итак, что мы имеем? А имеем мы список, в котором хранятся 4 имени файла, и нужно превратить их в ссылки.
# Вероятно, вы уже догадались, как это сделать. Если вы предположили, что это будет f''-строка, то вы совершенно правы.
#
# Давайте проанализируем, как формируется ссылка на пагинацию, и сформируем схему, которая поможет генерировать
# корректные ссылки.
#
# За схемой далеко ходить не нужно, в адресной строке мы можем ее увидеть.
# stepik-parsing.ru/html/index1_page_3.html
# Создадим переменную shema и сохраним в нее первую часть ссылки. И в цикле на каждой итерации мы будем склеивать
# обе части, чтобы получить корректную ссылку.
from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find('div', class_='pagen').find_all('a')

list_link = []
shema = 'http://parsinger.ru/html/'
'''for link in pagen:
    list_link.append(f"{shema}{link['href']}")'''
list_link = [f"{shema}{link['href']}" for link in pagen]
print(list_link)

# >>> ['http://parsinger.ru/html/index1_page_1.html', 'http://parsinger.ru/html/index1_page_2.html',
#      'http://parsinger.ru/html/index1_page_3.html', 'http://parsinger.ru/html/index1_page_4.html']
# Отлично, всё получилось.

# https://stepik.org/lesson/700334/step/3?unit=700275
# 1. Откройте сайт = http://parsinger.ru/html/index3_page_1.html
# 2. Извлеките названия товара с каждой страницы (всего 4х страниц)
# 3. Данные с каждой страницы должны храниться в списке.
# 4. По итогу работы должны получится 4 списка которые хранятся в списке(список списков)
# 5. Отправьте получившийся список списков в поле ответа.
# 6. Метод strip()использовать не нужно
# 7. Пример ожидаемого списка
#
# [[' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N'],
# [' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N']]
from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find('div', class_='pagen').find_all('a')
list_link = []
shema = 'http://parsinger.ru/html/'
for link in pagen:
    list_link.append(f"{shema}{link['href']}")
answer = []
for link in list_link:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name_items = soup.find_all('a', class_="name_item")
    name_items_list = []
    for name in name_items:
        name_items_list.append(name.text)
    answer.append(name_items_list)
print(answer)

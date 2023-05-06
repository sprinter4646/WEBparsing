# https://stepik.org/lesson/700334/step/5?unit=700275
# 1. Открываем сайт=http://parsinger.ru/html/index1_page_1.html
# 2. Проходимся по всем категориям, страницам и карточкам с товарами(всего 160шт)
# 3. Собираем с каждой карточки стоимость товара умножая, на количество товара в наличии
# 4. Складываем получившийся результат
# 5. Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.

# Павел Хошев в прошлом году
import requests
from bs4 import BeautifulSoup

url = 'http://parsinger.ru/html/index1_page_1.html'  # ошибка в адресе , поменяли везде stepik-parsing на parsinger
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

pagen = int(soup.find('div', 'pagen').find_all('a')[-1].text)  # определяем количество страниц
category = ['х' for x in soup.find('div', 'nav_menu').find_all('a')]  # формируем список из страниц с категориями
# товаров, чтобы для определить цикл по категориям, сократили

results = []
for x in range(1, len(category)+1):
    for i in range(1, pagen+1):  # Может оказаться что в разных категориях будет разное количество подстраниц?
        url = f'http://parsinger.ru/html/index{x}_page_{i}.html'  # формируем ссылки на карточки товаров
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        # name = [x.text.strip() for x in soup.find_all('a', 'name_item')] #  нигде не используется
        link = [f"http://parsinger.ru/html/{x['href'].strip()}" for x in soup.find_all('a', class_='name_item')]
        # Список ссылок
        result = [int(x.text.strip().split()[0]) for x in soup.find_all('p', 'price')]

        for li, res in zip(link, result):
            response = requests.get(url=li)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            count = int(soup.find('span', id='in_stock').string.split(':')[1])
            results.append(res * count)
print(sum(results))
# 45067195

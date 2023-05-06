# https://stepik.org/lesson/700334/step/5?unit=700275
# 1. Открываем сайт=http://parsinger.ru/html/index1_page_1.html
# 2. Проходимся по всем категориям, страницам и карточкам с товарами(всего 160шт)
# 3. Собираем с каждой карточки стоимость товара умножая, на количество товара в наличии
# 4. Складываем получившийся результат
# 5. Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.
from bs4 import BeautifulSoup
import requests

res = 0
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        url = f"https://parsinger.ru/html/{index_labels[i + 1]}/{i + 1}/{i + 1}_{j + 1}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        price_item = soup.find('span', id="in_stock").text
        price_item = int(price_item.strip('В наличии: '))
        quantity_item = soup.find('span', id="price").text
        quantity_item = int(quantity_item.strip(' руб'))
        res += price_item * quantity_item
print(res)
# 45067195

# https://stepik.org/lesson/700231/step/7?unit=700173
# 1. Открываем сайт = http://parsinger.ru/html/hdd/4/4_1.html
# 2. Получаем данные при помощи bs4 о старой цене и новой цене
# 3. По формуле высчитываем процент скидки
# 4. Формула (старая цена - новая цена) * 100 / старая цена)
# 5. Вставьте получившийся результат в поле ответа
# 6. Ответ должен быть числом с 1 знаком после запятой.

from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = int(soup.find('span', id="price").text.replace(' руб', ''))
div_old = int(soup.find('span', id="old_price").text.replace(' руб', ''))
res = ((div_old - div) / div_old) * 100
print(round(res, 1))
# res = 19.7


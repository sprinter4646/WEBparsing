# https://stepik.org/lesson/700334/step/4?unit=700275
# 1. Открываем сайт=http://parsinger.ru/html/index3_page_4.html
# 2. Проходимся по всем страницам в категории мыши (всего  4 страницы)
# 3. На каждой странице посещаем каждую карточку с товаром (всего 32 товаров)
# 4. В каждой карточке извлекаем при помощи bs4 артикул <p class="article"> Артикул: 80244813 </p>
# 5. Складываем(плюсуем) все собранные значения
# 6. Вставляем получившийся результат в поле ответа
#
from bs4 import BeautifulSoup
import requests
res = 0
for i in range(1, 33):
    i_card = f'https://parsinger.ru/html/mouse/3/3_{i}.html'
    response = requests.get(url=i_card)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    art_i = soup.find('p', class_='article').text
    print(art_i[-8:])
    res += int(art_i[-8:])
print(res)

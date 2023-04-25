# https://stepik.org/lesson/896231/step/2?unit=901222
# soup.find_all() - это метод Beautiful Soup, который ищет все элементы в HTML-документе, соответствующие переданным
# параметрам. Возвращает список элементов Beautiful Soup, которые удовлетворяют условиям поиска.
#
# soup.find_all(self, name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)
# Параметры:
#
# name - имя тега HTML, который нужно найти. Опциональный параметр.
# attrs - словарь атрибутов и их значений, которые нужно найти. Опциональный параметр.
# text - текст, который нужно найти. Опциональный параметр.
# limit - максимальное количество элементов, которые мы хотим найти. Опциональный параметр.
# recursive - определяет, должны ли мы искать элементы во вложенных тегах. По умолчанию True. Опциональный параметр.
# Пример 2
#
# Используем метод .find_all для поиска всех тегов a с атрибутом href. Результат записывается в переменную result.
# Далее в цикле for перебирается список тегов и выводится значение атрибута href и текст внутри тега.
# В итоге будет выведено две строки: значение href и текст для каждого тега a.
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
        <a href="https://google.com">Google</a>
        <a href="https://yandex.ru">Yandex</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `a` с атрибутом href
result = soup.find_all('a', href=True)
for tag in result:
    print(tag['href'], tag.text)



# https://stepik.org/lesson/715854/step/4?unit=716645

# Cookies на практике
# Когда мы знаем имена всех cookie на странице, мы можем получить нужные нам данные по ключу. Мы помним, что
# .get_cookies() возвращает список словарей.  Если вы посмотрите на первый пример с кодом, вы увидите, что в cookie
# хранится время экспирации 'expiry': 1685518907 т.е., время истечения срока жизни cookie. Пример кода ниже поможет нам
# извлечь конкретное значение из cookie.
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    print(webdriver.get_cookie('yandex_gid')['expiry'])

# >>>1688201210

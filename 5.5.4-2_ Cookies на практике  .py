# https://stepik.org/lesson/715854/step/4?unit=716645

# Cookies на практике
# .get_cookie(name_cookie)
# В отличие от первого метода, этот метод находит и возвращает cookie по его имени. Есть два способа определить имя.
#
# Способ №1 - этот способ не очень надежен, т.к. с "живого" браузера данные в cookies могут отличаться в зависимости от
# открытой сессии. Но если ваш код не зависит от параметров сессии, то можно получить имена cookie именно в браузере;
#
# Способ №2 - мы можем в цикле for/in итерироваться по списку cookie, который мы получили с помощью метода
# .get_cookies() . Этим способом мы можем получить не только имя cookie, но и его значение.
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://ya.ru/')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        print(cookie['name'])  # или cookie['value'] чтобы получить их значение
        print(cookie['value'])  # или cookie['value'] чтобы получить их значение

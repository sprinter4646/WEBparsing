# https://stepik.org/lesson/715854/step/6?unit=716645

# ЗАДАЧА
# Откройте сайт=https://parsinger.ru/methods/3/index.html с помощью Selenium;
# На сайте есть определённое количество секретных cookie;
# Так что же такое "секретные" куки? Я тупо просуммировал все значения поля 'value' во всех куках и ответ оказался
# правильным... Как-то это не очень внятно.
# Ваша задача получить все значения и суммировать их;
# Полученный результат вставить в поле для ответа.
from pprint import pprint
import time
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    res = sum([int(cookie['value']) for cookie in cookies])
    print(res)
    time.sleep(10)
# >4901217

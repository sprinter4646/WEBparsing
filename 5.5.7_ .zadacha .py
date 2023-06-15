# https://stepik.org/lesson/715854/step/7?unit=716645

# ЗАДАЧА
# Откройте сайт=https://parsinger.ru/methods/3/index.html с помощью Selenium;
# Ваша задача получить все значения cookie с чётным числом после "_" и суммировать их;
# Полученный результат вставить в поле для ответа.
from pprint import pprint
import time
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    res = 0
    for cookie in cookies:
        if int(cookie['name'][-1]) % 2 == 0:
            res += int(cookie['value'])
    print(res)
    time.sleep(10)
# >1962101

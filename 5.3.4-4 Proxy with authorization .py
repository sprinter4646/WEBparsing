# https://stepik.org/lesson/716118/step/4?auth=login&unit=716910
# Proxy и Selenium
# Proxy with authorization
# Proxy с авторизацией
# Для настройки прокси с авторизацией вам потребуется отдельно установить расширение seleniumwire.
#
# Делается это так:
#
# Установка
#
# pip install selenium-wire
#
#
# Импорт
#
# from seleniumwire import webdriver
# Если у вас есть рабочий прокси, используйте его, или приобретите за 100 р/шт в магазине https://proxy6.net/,
# для запуска следующего кода(прокси в примере ниже, может не работать).
import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

options = {'proxy': {
    'http': "socks5://GVFJNw:yneWoN@45.10.81.217:8000",
    'https': "socks5://GVFJNw:yneWoN@45.10.81.217:8000",
    }}

url = 'https://2ip.ru/'

with webdriver.Chrome(seleniumwire_options=options) as browser:
    browser.get(url)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
    time.sleep(5)

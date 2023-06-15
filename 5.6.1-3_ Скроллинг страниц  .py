# https://stepik.org/lesson/715954/step/1?unit=716748

# 5.6 Скроллинг страниц
# Прокрутка содержимого страницы - способ 1 execute_script()
# Представим, что у вас сайт, который имеет разные высоты страницы. Мы можем получить значение высоты непосредственно
# той части сайта, которая попадает в область вашей видимости, или значение высоты сайта полностью.
#
# return document.body.scrollHeight вернёт значение высоты основного элемента на странице -  body
import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    height = browser.execute_script("return document.body.scrollHeight")
    time.sleep(2)
    print(height)

# >>>81000
# 81000 пикселей имеет в высоту наш сайт.

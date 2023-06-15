# https://stepik.org/lesson/715954/step/1?unit=716748

# 5.6 Скроллинг страниц
# Прокрутка содержимого страницы - способ 1 execute_script()
# Напишем простой код, который прокрутит страницу в низ.

import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    for i in range(10):
        browser.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)
# Мы сделали 10 итераций и не оказались в самом низу страницы. Потому что мы не знаем, сколько пикселей имеет в высоту
# наш сайт. Мы можем использовать большие значения, к примеру,  window.scrollBy(0,500000), такие большие цифры за один
# скроллинг способы прокрутить всю страницу. И это то, что вы будете делать, когда у вас обычный сайт
# без прогрузки данных.

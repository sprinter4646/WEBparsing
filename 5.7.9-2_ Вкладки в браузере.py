# https://stepik.org/lesson/720527/step/9?unit=721524

# Вкладки в браузере
# В некоторых гайдах в интернете, вы будете встречать информацию о том, что работать вы можете только в первой, открытой
# вкладке, а остальные открываются для красоты. Но хочу вас обрадовать, это совсем не так. Работать мы можем со всеми
# вкладками, но только по очереди и только в активной.
#
# Запустите у себя в терминале код ниже, чтобы наблюдать работу Selenium во всех вкладках по очереди. Обратите внимание
# на то, что мы получаем длину списка. Обратите внимание и на то, что итерация по вкладкам происходит в обратном порядке
# , от последней к первой, чтобы этого избежать, просто добавляем к циклу функцию reversed(). Так же следует обратить
# внимание на, что самая первая вкладка имеет имя data; в этой вкладке открывается страница, переданная в метод
# .get("URL")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://stepik.org/course/104774/promo")
    # Вместо вкладки data; будет вкладка в которой будет загружен степик
    browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

    for x in reversed(range(len(browser.window_handles))):
        # reversed(range(len(browser.window_handles))) Для итерирования по порядку ?(1,3,2,4)
        browser.switch_to.window(browser.window_handles[x])
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()
        time.sleep(3)



# https://stepik.org/lesson/715954/step/4?unit=716748

# Когда вы хотите взаимодействовать с элементом, который визуально перекрыт другим элементом, вы получите ошибку.
#
# selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
# Element <button class="btn" onclick="clicks()">...</button> is not clickable at point (135, 179).
# Other element would receive the click: <div class="block2"></div>
# Это ошибка нам сообщает, что другой элемент получит клик. Для того чтобы исключить такие ситуации, нам необходимо
# получить фокус этого элемента. webdriver перед кликом проверяет ширину и высоту элемента, если они больше 0,
# то клик будет произведён по центру элемента. Для того чтобы получить фокус элемента, можно использовать
#
# browser.find_element(By.ID, 'btn')
#
# element = browser.find_element(By.CLASS_NAME, 'btn')
# browser.execute_script("return arguments[0].scrollIntoView(true);", element) где element это объект webdriver'a.
#
#
# Задача:
#
# Откройте сайт=http://parsinger.ru/scroll/4/index.html с помощью Selenium;
# На сайте есть 50 кнопок, которые визуально перекрыты блоками;
# После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число;
# Цель: написать скрипт, который нажимает поочерёдно все кнопки и собирает уникальные числа;
# Все полученные числа суммировать, и вставить результат в поле для ответа.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/4/index.html')
    bttns = browser.find_elements(By.CLASS_NAME, 'btn')
    answer = 0
    for x in bttns:
        browser.execute_script("return arguments[0].scrollIntoView(true);", x)
        x.click()
        bttn_n = browser.find_element(By.ID, 'result')
        answer += int(bttn_n.text)
    print(answer)
# >>>4479945576993

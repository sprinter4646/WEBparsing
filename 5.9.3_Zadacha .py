# https://stepik.org/lesson/897512/step/3?unit=902579

# Zadacha
# Откройте сайт=https://parsinger.ru/draganddrop/2/index.html c помощью Selenium;
# На сайте есть четыре пронумерованных блока;
# Напишите скрипт который перетащит красный квадрат поочерёдно в каждый блок;
# После перемещения красного квадрата по всем блокам , появится токен, вставьте его в поле для ответа;

import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    time.sleep(3)
    drag = browser.find_element(By.XPATH, '//*[@id="draggable"]')
    final = browser.find_elements(By.CLASS_NAME, 'box')
    actions = ActionChains(browser)
    for box in final:
        actions.drag_and_drop(drag, box).perform()
    result = browser.find_element(By.ID, 'message').text
    print(result)

# >>> NS4zNDUzMzU0NTQ2MzU0NDVlKzIx

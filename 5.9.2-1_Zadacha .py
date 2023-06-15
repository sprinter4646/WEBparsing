# https://stepik.org/lesson/897512/step/2?unit=902579

# Zadacha
# Откройте сайт=https://parsinger.ru/draganddrop/1/index.html c помощью Selenium;
# Напишите скрипт который перетащит красный блок из первого поля во второе;
# После перемещения блока, появится токен, вставьте его в поле для ответа;

# Павел Хошев 4 месяца назад
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    time.sleep(3)
    drag = browser.find_element(By.XPATH, '//*[@id="draggable"]')
    final = browser.find_element(By.XPATH, '//*[@id="field2"]')
    actions = ActionChains(browser)

    actions.drag_and_drop(drag, final).perform()
    result = browser.find_element(By.ID, 'result').text
    print(result)

# >>> ODYzNDQ1MzM0NTE0MzQ2OTAwMA==

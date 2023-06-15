# https://stepik.org/lesson/720527/step/2?unit=721524

# Zadacha
# Откройте сайт=http://parsinger.ru/blank/modal/2/index.html при помощи Selenium;
# На сайте есть 100 buttons;
# При нажатии на одну из кнопок в  теге <p id="result">Code</p> появится код;
# Вставьте секретный код в поле для ответа.
# Павел Хошев в прошлом году
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/2/index.html')
    time.sleep(.5)

    for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
        button.click()
        browser.switch_to.alert.accept()
        result = browser.find_element(By.ID, 'result').text
        if result:
            print(result)
            break
# >>>321968541687435564865796413874

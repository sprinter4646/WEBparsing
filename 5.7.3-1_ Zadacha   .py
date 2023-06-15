# https://stepik.org/lesson/720527/step/3?unit=721524

# Zadacha
# Откройте сайт=http://parsinger.ru/blank/modal/3/index.html при помощи Selenium;
# На сайте есть 100 buttons;
# При нажатии на любую кнопку появляется confirm с пин-кодом;
# Текстовое поле под кнопками проверяет правильность пин-кода;
# Ваша задача, найти правильный пин-код и получить секретный код;
# Вставьте секретный код в поле для ответа.
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/3/index.html')

    for button in browser.find_elements(By.TAG_NAME, 'input'):
        button.click()
        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        browser.find_element(By.ID, 'input').send_keys(pin)
        browser.find_element(By.ID, 'check').click()
        res = browser.find_element(By.ID, 'result').text
        if res != 'Неверный пин-код':
            print(res)
            break
# >>>867413857416874163897546183542

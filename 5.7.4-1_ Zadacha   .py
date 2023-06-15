# https://stepik.org/lesson/720527/step/4?unit=721524

# Zadacha
# Откройте сайт=http://parsinger.ru/blank/modal/4/index.html при помощи Selenium;
# На сайте есть список пин-кодов и только один правильный;
# Для проверки пин-кода используйте кнопку "Проверить"
# Ваша задача, найти правильный пин-код и получить секретный код;
# Вставьте секретный код в поле для ответа.
# UPD: Очень часто студенты при решении этой задачи сталкиваются с одной и той же проблемой, пытаясь отправить в
# модальное окно browser.send_keys(elem.text) так делать нельзя. В метод send_keys("text") должен быть передан строковый
# тип данных. Передавать в метод вебэлемент и преобразовывать его внутри метода большая ошибка, для корректной работы
# текст из элемента должен быть извлечён заранее.
#
# Примерно вот так.
# for pin in pin_codes:
#    pin.text
#    browser.send_keys(pin)
#  А так не правильно.
#
# for pin in pin_codes:
#    browser.send_keys(pin.text)

# Павел Хошев в прошлом году
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/4/index.html')
    pin_code = [x.text for x in browser.find_elements(By.CLASS_NAME, 'pin')]
    for pin in pin_code:
        browser.find_element(By.ID, 'check').click()
        confirm = browser.switch_to.alert
        time.sleep(.3)
        confirm.send_keys(pin)
        confirm.accept()
        result = browser.find_element(By.ID, 'result').text
        if result.isdigit():
            print(result)

# >>>1261851212132345456274632

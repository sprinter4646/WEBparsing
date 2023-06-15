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

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/4/index.html')
    pin_list = browser.find_elements(By.TAG_NAME, 'span')
    print(pin_list)
    for pin in pin_list:
        print(pin.text)
        a = browser.find_element(By.TAG_NAME, 'input')
        a.click()
        a = browser.switch_to.alert
        # a.send_keys(pin)
        time.sleep(10)
        a.accept()
    # check_btn.click()
    # browser.find_element(By.ID, 'input').send_keys(pin)
    # res = browser.find_element(By.ID, 'result').text
    # if res != 'Неверный пин-код':
    #     print(pin.text)
    #     break

# >>>1261851212132345456274632

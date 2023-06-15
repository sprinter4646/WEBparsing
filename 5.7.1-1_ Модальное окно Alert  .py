# https://stepik.org/lesson/720527/step/1?unit=721524

# ЗМодальное окно Alert
# Код ниже, выполнит клик на кнопку с id="alert", вызвав тем самым модальное окно alert, переключит на него свой фокус
# функцией browser.switch_to.alert и в принте распечатает содержимое title этого окна.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'alert').click()
    time.sleep(1)
    alert = browser.switch_to.alert  # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
    print(alert.text)
    time.sleep(1)
    alert.accept()

# >>> Это модальное окно alert

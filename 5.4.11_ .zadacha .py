# https://stepik.org/lesson/709437/step/11?unit=710000
# Откройте сайт=http://parsinger.ru/selenium/4/4.html;
# Установите все чек боксы в положение checked при помощи selenium и метода click();
# <input type="checkbox" class="check" value="1">
# Когда все чек боксы станут активны, нажмите на кнопку;
# Скопируйте число которое появится на странице;
# Результат появится в <p id="result">Result</p>;
# Вставьте число в поле для ответа.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/4/4.html')
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'check')]
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)
# >>>3,1415926535897932384626433832795028841971

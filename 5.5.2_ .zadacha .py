# https://stepik.org/lesson/715854/step/2?unit=716645

# ЗАДАЧА
# Откройте сайт=https://parsinger.ru/methods/1/index.html с помощью Selenium;
# При обновлении сайта, в id="result" появится число;
# Обновить страницу возможно придется много раз, т.к. число появляется не часто;
# Вставьте полученный результат в поле для ответа:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
viragenie = 74604646177
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    res = browser.find_element(By.ID, 'result').text
    while res == 'refresh page':
        browser.refresh()
        res = browser.find_element(By.ID, 'result').text
    print(res)
# >>>4168138981270992

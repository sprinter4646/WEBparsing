# https://stepik.org/lesson/709437/step/14?unit=710000

# ЗАДАЧА
# Откройте сайт=http://parsinger.ru/selenium/6/6.html при помощи selenium;
# Найдите значение выражения на странице ((12434107696 * 3) * 2) + 1=74604646177;
# Найдите и выберите в  выпадающем списке элемент с числом,
# которое у вас получилось после нахождения значения уравнения;
# Нажмите на кнопку;
# Скопируйте число и вставьте в поле ответа=98763216843164361841357461685743168461.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
viragenie = 74604646177
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/6/6.html')
    res = eval(browser.find_element(By.ID, "text_box").text)
    browser.find_element(By.ID, 'selectId').send_keys(res)
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, 'result').text)
# >>>74604646177
# >>>98763216843164361841357461685743168461

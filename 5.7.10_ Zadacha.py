# https://stepik.org/lesson/720527/step/10?unit=721524

# Zadacha
# ткройте сайт=http://parsinger.ru/blank/3/index.html с помощью Selenium;
# На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке;
# Каждая вкладка имеет в title уникальное число;
# Цель - собрать числа с каждой вкладки и суммировать их;
# Полученный результат вставить в поле для ответа.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/blank/3/index.html")
    for x, y in zip(browser.window_handles, browser.find_elements(By.CLASS_NAME, 'buttons')):
        y.click()
        browser.switch_to.window(x)
        time.sleep(2)
        print(browser.execute_script("return document.title;"))


# >>>


# https://stepik.org/lesson/720527/step/10?unit=721524

# Zadacha
# ткройте сайт=http://parsinger.ru/blank/3/index.html с помощью Selenium;
# На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке;
# Каждая вкладка имеет в title уникальное число;
# Цель - собрать числа с каждой вкладки и суммировать их;
# Полученный результат вставить в поле для ответа.
# Павел Хошев в прошлом году
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    count = 0
    browser.get('http://parsinger.ru/blank/3/index.html')
    [x.click() for x in browser.find_elements(By.CLASS_NAME, 'buttons')]
    tabs = browser.window_handles
    for tab in range(len(tabs)):
        browser.switch_to.window(browser.window_handles[tab])
        title = browser.execute_script("return document.title;")
        if title.isdigit():
            count += int(title)
    print(count)
# >>>77725787998028643152187739088279

# >>>


# https://stepik.org/lesson/720527/step/4?unit=721524
import time

# Zadacha
# Откройте сайт=http://parsinger.ru/window_size/2/index.html с помощью selenium;
# У вас есть 2 списка с размерами  size_x и size_y;
# При сочетании размеров из этих списков, появится число;
# Только при единственном сочетании размеров из этих списков, появится число;
# Результат появится в id="result";
# Скопируйте результат в поле для ответа.
# ps. При написании кода, учитывайте размер рамок браузера.
#
# window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

import time

import headless as headless
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome("path/to/chromedriver.exe", options=options)
    browser.get('http://parsinger.ru/window_size/1/index.html')
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    for x in window_size_x:
        for y in window_size_y:
            # browser(--headless)
            browser.set_window_size(x, y)  # x+44, y+171
            time.sleep(0.2)
            res = browser.find_element(By.XPATH, '//*[@id="result"]')
            print(res.text)
            print(browser.find_element(By.ID, 'result').text)`

            '''if res.isdigit():
                print(res)
            # time.sleep(1)'''

# >>>нет ответа

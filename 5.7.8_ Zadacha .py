# https://stepik.org/lesson/720527/step/8?unit=721524

# Zadacha
# Для этой задачи потребуется код с прошлого степа.
#
# Откройте сайт=http://parsinger.ru/window_size/2/index.html с помощью selenium;
# У вас есть 2 списка с размера окон size_x и size_y;
# Цель: определить размер окна, при котором,  в id="result" появляется число;
# Результат должен быть в виде словаря {'width': size_x, 'height': size_y}
# ps. При написании кода, учитывайте размер рамок браузера.
#
# Метод .get_window_size() возвращает словарь с размерами окна.
#
# Размеры рамок могут зависеть от вашего разрешения и масштабирования экрана. Задача составлена при 100%
# масштабировании, масштабирование можно проверить в настройках дисплея.
#
# window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
# window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# На вход ожидается словарь  {'width': 000, 'height':000} где размеры указаны без учёта размеров рамок браузера, т.е.
# необходимо указать размер рабочей области браузера.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser.get('http://parsinger.ru/window_size/2/index.html')
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x + 44, y + 171)  # x+44, y+171
            # time.sleep(0.2)
            res = browser.find_element(By.XPATH, '//*[@id="result"]')
            # print(res.text)
            # print(browser.find_element(By.ID, 'result').text)
            if res.text.isdigit():
                print(res.text)
                print(x, y)
                print(browser.get_window_size())

# >>>9874163854135461654
# 955 600
# {'width': 999, 'height': 771}
# answer={'width': 955, 'height': 600}

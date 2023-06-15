# https://stepik.org/lesson/720527/step/6?unit=721524

# Zadacha
# Откройте сайт=http://parsinger.ru/window_size/1/ с помощью selenium;
# Необходимо открыть окно таким размером, чтобы рабочая область страницы составляла 555px на 555px;
# Учитывайте размеры границ браузера;
# Результат появится в id="result";
# Вставьте полученный результат в поле для ответа.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    width = 599  # width=555+44 height=555+171 мой комп с убунту
    height = 726  # height=555+171
    browser.set_window_size(width, height)
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(5)

# >>>1684163857416385746374

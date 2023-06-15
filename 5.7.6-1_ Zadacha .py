# https://stepik.org/lesson/720527/step/6?unit=721524

# Zadacha
# Откройте сайт=http://parsinger.ru/window_size/1/ с помощью selenium;
# Необходимо открыть окно таким размером, чтобы рабочая область страницы составляла 555px на 555px;
# Учитывайте размеры границ браузера;
# Результат появится в id="result";
# Вставьте полученный результат в поле для ответа.
# Павел Хошев в прошлом году
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/index.html')
    browser.set_window_size(555 + 16, 555 + 133)
    print(browser.find_element(By.ID, 'result').text)

# >>>нет ответа

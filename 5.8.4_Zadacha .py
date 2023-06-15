# https://stepik.org/lesson/715955/step/4?unit=716749

# Zadacha
# Откройте сайт=http://parsinger.ru/expectations/3/index.html при помощи Selenium;
# На сайте есть кнопка, которая становится активной после загрузки страницы с рандомной задержкой, от 1 до 3 сек;
# После нажатия на кнопку, в title начнут появляться коды, с рандомным временем, от 0.1 до 0.6 сек;
# Ваша задача успеть скопировать код из id="result", когда  title будет равен "345FDG3245SFD";
# Вставить  появившийся  код в поле для ответа.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/3/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    for x in range(53):
        time.sleep(0.6)
        if browser.execute_script("return document.title;") == '345FDG3245SFD':
            print(browser.find_element(By.ID, 'result').text)
            print(browser.execute_script("return document.title;"))
# >>>82934401788.40141

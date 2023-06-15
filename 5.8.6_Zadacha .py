# https://stepik.org/lesson/715955/step/6?unit=716749

# Zadacha
# В этой задаче используйте метод presence_of_element_located(locator) который проверяет наличие элемента в DOM.
#
# Откройте сайт=http://parsinger.ru/expectations/5/index.html при помощи Selenium;
# На сайте есть кнопка, поведение которой вам знакомо;
# После нажатие на кнопку, на странице начнётся создание элементов class с рандомными значениями;
# Ваша задача применить метод, чтобы он вернул содержимое элемента с классом "BMH21YY", когда он появится на странице;
# Полученное значение вставить в поле для ответа.
# ps. Вы конечно можете и в ручную найти элемент с этим классом, но кого вы обманите?
# <div class="BMH21YY"> 688596737976</div>
#
# Введите численный ответ

# Павел Хошев в прошлом году
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://parsinger.ru/expectations/5/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    el = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY')))
    print(el.text)

# >>> 688596737976

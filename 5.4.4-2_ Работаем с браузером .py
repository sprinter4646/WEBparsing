# https://stepik.org/lesson/709437/step/4?unit=710000
# Работаем с браузером
# Если ошибка произойдет во время выполнения кода до команды .quit() , сеанс WebDriver не будет закрыт должным образом,
# и файлы не будут удалены из памяти.
#
# Для того, чтобы код гарантированно завершил свою работу командой  browser.quit(), используем конструкцию  try/finally.
# Весь код после finally: будет гарантированно выполнен.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    browser.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = browser.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)
finally:
    browser.quit

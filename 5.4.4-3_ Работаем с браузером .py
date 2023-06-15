# https://stepik.org/lesson/709437/step/4?unit=710000
# Работаем с браузером
# Но есть еще третий способ, мой любимый, -  это менеджер контекста with/as. С этим способом нам вообще не нужно думать
# о том, когда закрывать браузер, менеджер контекста делает это за нас в тот момент, когда это нужно.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = browser.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)

# https://stepik.org/lesson/720527/step/1?unit=721524

# Модальное окно Confirm
# Модальное окно confirm имеет всего 2 кнопки, "Ok" и "Отмена", взаимодействовать с которыми мы можем функциями
# .accept()  и .dismiss()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'confirm').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
    time.sleep(.5)

# Код выше, нажимает на кнопку Confirm и в появившемся окне нажимает на кнопку "Ok"

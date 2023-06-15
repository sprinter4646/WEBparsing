# https://stepik.org/lesson/897512/step/2?unit=902579

# Zadacha
# Откройте сайт=https://parsinger.ru/draganddrop/1/index.html c помощью Selenium;
# Напишите скрипт который перетащит красный блок из первого поля во второе;
# После перемещения блока, появится токен, вставьте его в поле для ответа;

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://parsinger.ru/draganddrop/1/index.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    # Находим исходный элемент, который будет перемещать
    source_element = browser.find_element(By.ID, "field1")

    # Находим целевой элемент, куда будем перемещать иcходный элемент
    target_element = browser.find_element(By.ID, "field2")

    # Создаём экземпляр класса ActionChains
    actions = ActionChains(browser)

    # Выполняем действие перетаскивания
    actions.drag_and_drop(source_element, target_element).perform()

    print(browser.find_element(By.ID, 'result').text)

# >>> ODYzNDQ1MzM0NTE0MzQ2OTAwMA==

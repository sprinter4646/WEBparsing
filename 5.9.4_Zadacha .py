# https://stepik.org/lesson/897512/step/4?unit=902579

# Откройте сайт=https://parsinger.ru/draganddrop/3/index.html c помощью Selenium;
# На сайте есть синий квадрат, который нужно перетащить по оси X ;
# Напишите скрипт который перетащит синий квадрат поочерёдно через все красные точки;
# После перемещения синего квадрата по всем точкам, появится токен, вставьте его в поле для ответа;
#
# Подсказка: используйте вместе .click_and_hold() и .move_by_offset()

import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    time.sleep(3)
    drag = browser.find_element(By.ID, 'block1')
    final = browser.find_elements(By.CLASS_NAME, 'controlPoint')
    actions = ActionChains(browser)
    for point in final:
        actions.click_and_hold(drag).perform()
        # actions.move_to_element(point).release(point).perform()
        actions.move_by_offset(50, 0).perform()
    actions.release().perform()
    time.sleep(3)
    result = browser.find_element(By.ID, 'message')
    print(result.text)

# >>>
# Ni44NTc4MTk2NzY4NTQ0NTZlKzIz

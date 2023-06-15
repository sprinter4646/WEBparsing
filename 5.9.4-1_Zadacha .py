# https://stepik.org/lesson/897512/step/4?unit=902579

# Откройте сайт=https://parsinger.ru/draganddrop/3/index.html c помощью Selenium;
# На сайте есть синий квадрат, который нужно перетащить по оси X ;
# Напишите скрипт который перетащит синий квадрат поочерёдно через все красные точки;
# После перемещения синего квадрата по всем точкам, появится токен, вставьте его в поле для ответа;
#
# Подсказка: используйте вместе .click_and_hold() и .move_by_offset()

# Павел Хошев 4 месяца назад
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    time.sleep(1)
    drag = browser.find_element(By.ID, 'block1')
    actions = ActionChains(browser)
    lst = [10]*400
    actions.click_and_hold(drag)
    for x in lst:
        actions.move_by_offset(x, 0)
    actions.perform()
    time.sleep(5)
# >>>
# Ni44NTc4MTk2NzY4NTQ0NTZlKzIz

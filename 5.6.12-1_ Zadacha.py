# https://stepik.org/lesson/715954/step/12?unit=716748

# Задача
# Для скроллинга окна используйте .scroll_by_amount(delta_x, delta_y)
#
# Откройте сайт=http://parsinger.ru/infiniti_scroll_2/ с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# Необходимо прокрутить окно в самый низ;
# Цель: получить все значение в элементах, сложить их;
# Получившийся результат вставить в поле ответа.

# Павел Хошев 10 месяцев назад
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    url = 'http://parsinger.ru/infiniti_scroll_2/'
    browser.get(url)
    browser.set_window_size(1920, 1080)
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    while True:
        ActionChains(browser).move_to_element(div).scroll_by_amount(800, 400).perform()
        time.sleep(0.2)
        attrbt = [x.get_attribute('id') for x in browser.find_elements(By.TAG_NAME, 'p') if x.get_attribute('class')]
        if attrbt:
            break
    res = [int(x.text) for x in browser.find_elements(By.TAG_NAME, 'p') if x.text]
    print(sum(res))
# >>>499917600

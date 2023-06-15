# https://stepik.org/lesson/715954/step/13?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/infiniti_scroll_3/ с помощью Selenium
# На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100 элементов;
# Необходимо прокрутить все окна в самый низ;
# Цель: получить все значение в каждом из окошек и сложить их;
# Получившийся результат вставить в поле ответа.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_3/')
    divs = []
    for i in range(1, 6):
        div = (browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div'))
        for _ in range(8):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
    names = [int(i.text) for i in browser.find_elements(By.TAG_NAME, 'span') if i.text]
    print(sum(names))

    time.sleep(3)
# >>>159858750

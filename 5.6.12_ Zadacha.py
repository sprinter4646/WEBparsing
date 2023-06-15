# https://stepik.org/lesson/715954/step/12?unit=716748

# Задача
# Для скроллинга окна используйте .scroll_by_amount(delta_x, delta_y)
#
# Откройте сайт=http://parsinger.ru/infiniti_scroll_2/ с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# Необходимо прокрутить окно в самый низ;
# Цель: получить все значение в элементах, сложить их;
# Получившийся результат вставить в поле ответа.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    while True:
        try:
            if browser.find_element(By.CLASS_NAME, 'last-of-list'):
                print('THE END OF SCROLL LIST IS FOUND')
                names = [int(i.text) for i in browser.find_elements(By.TAG_NAME, 'p') if i.text]
                print(sum(names))
                break
        except:
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
# >>>499917600

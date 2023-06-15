# https://stepik.org/lesson/715954/step/7?unit=716748

# Если мы знаем, какой длины список, мы можем использовать цикл for. Если вы уверены, что вам хватит прокрутить
# элемент 10 раз по 500px, то можно использовать такой подход.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

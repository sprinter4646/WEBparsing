# https://stepik.org/lesson/715954/step/5?unit=716748

# Прокрутка содержимого страницы - способ 2 Keys()
# Для того чтобы взаимодействовать подобным образом с остальными элементами <input>, нам уже потребуется цикл while,
# если мы не знаем точного количества элементов, или цикл for если точное количество элементов нам известно.
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    tags_input = browser.find_elements(By.TAG_NAME, 'input')

    for input in tags_input:
        input.send_keys(Keys.DOWN)
        time.sleep(1)
# Запустите этот код у себя в терминале и вы увидите, что этот код поочередно выделяет(берет в фокус) все <input> на
# странице.  Наш сайт-тренажер довольно примитивен и отдает весь список тегов <input> разом.

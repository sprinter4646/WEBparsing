# https://stepik.org/lesson/715954/step/10?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/infiniti_scroll_1/ с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
# Используйте Keys.DOWN или .move_to_element();
# Цель: получить все значение в элементах, сложить их;
# Получившийся результат вставить в поле ответа.
# Подсказка:
# Элементы могут грузится медленнее чем работает ваш код, установите задержки.
# Подумайте над условием прерывания цикла, последний элемент в списке имеет class="last-of-list"

# Кирилл Петрулевич 9 месяцев назад
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

URL = 'https://parsinger.ru/infiniti_scroll_1/'
# option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome() as browser:
    browser.get(URL)
    time.sleep(1)
    tag_p = browser.find_element(By.TAG_NAME, 'input')
    while True:
        tag_p.send_keys(Keys.DOWN)
        if browser.find_elements(By.CLASS_NAME, 'last-of-list'): break
    tag_p = browser.find_element(By.ID, 'scroll-container')
    print(sum(map(int, tag_p.text.split())))
# >>> 86049950

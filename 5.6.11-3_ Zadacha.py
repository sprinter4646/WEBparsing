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

# Gleb Drobiazko 6 месяцев назад
# Т.к.здесь не требуется прожимать каждый чекбокс, то можно просто прокрутить весь лист и уже искать в прогруженном коде

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(2)
    while True:
        try:
            if browser.find_element(By.CLASS_NAME, 'last-of-list'):
                print('THE END OF SCROLL LIST IS FOUND')
                names = [int(i.text) for i in browser.find_elements(By.TAG_NAME, 'span') if i.text]
                print(sum(names))
                break
        except:
            browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
# >>> 86049950

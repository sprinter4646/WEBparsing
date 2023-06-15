# https://stepik.org/lesson/715954/step/5?unit=716748

# Прокрутка содержимого страницы - способ 2 Keys()
# Второй способ прокрутки содержимого с использованием класса Keys() из модуля Selenium.
# Импортируем:
# from selenium.webdriver import Keys
# или
# from selenium.webdriver.common.keys import Keys
# Откроем наш сайт, на нем есть 100 тегов <input>, с которыми мы и будем взаимодействовать. Взаимодействовать мы можем
# только с интерактивными элементами -  это кнопки, ссылки, различные input`ы, и другие, а не интерактивные - это абзацы
# с текстом, различные элементы списка li и табличные элементы tr,td и другие. Для того чтобы лучше понять интерактивный
# элемент перед вами или нет, нажмите несколько раз клавишу TAB на клавиатуре, если элемент выделяется,
# то он интерактивный.
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    tag_p = browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
    time.sleep(10)
# Выполнив этот код у себя в терминале, вы увидите, что на открывшемся сайте получил выделение первый тег <input>,
# потому что метод .find_element() возвращает первый найденный элемент.


# https://stepik.org/lesson/709437/step/13?unit=710000
# Выпадающие списки
# Работа с выпадающими списками практически ничем не отличается от работы с чек боксами или полями.
#
# Для того чтобы получить значение любого элемента из выпадающего списка, мы может использовать привычные нам методы
# поиска элемента.
# <select id="opt">
#                   <option value="1">98016191141</option>
#                   <option value="2">48026291242</option>
# В нашем случае на нашем сайте все элементы выпадающего списка, могут быть спокойно найдены по тегу, метод By.TAG_NAME
# нам в этом поможет.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/selenium/6/6.html')
#     g = browser.find_element(By.TAG_NAME, 'option').text
#     print(g)
# >>>98016191141
# ЗАДАЧА
# Открываем сайт=http://parsinger.ru/selenium/7/7.html с помощью selenium;
# Получаем значения всех элементов выпадающего списка;
# Суммируем(плюсуем) все значения;
# Вставляем получившийся результат в поле на сайте;
# input type="text" id="input_result">
# Нажимаем кнопку и копируем длинное число;
# Вставляем конечный результат в поле ответа.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    g = browser.find_elements(By.TAG_NAME, 'option')
    res = sum(int(item.text) for item in g)
    browser.find_element(By.ID, 'input_result').send_keys(res)
    browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(5)
# >>>4194183965770
# >>>321687416587463168743416874641687

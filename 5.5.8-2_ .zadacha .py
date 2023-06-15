# https://stepik.org/lesson/715854/step/8?unit=716645

# ЗАДАЧА
# Откройте сайте=https://parsinger.ru/methods/5/index.html с помощью Selenium;
# На сайте есть 42 ссылки, у каждого сайта по ссылке есть cookie с определёнными сроком жизни;
# Цель: написать скрипт, который сможет найти среди всех ссылок страницу с самым длинным сроком жизни cookie и получить
# с этой страницы число;
# Вставить число в поле для ответа.
#
#
# UPD: После обновления Chrome до версии 104 метод Selenium .get_cookies() начал возвращать время эпохи(чтобы это не
# значило) именно поэтому этот метод начал возвращать значение +-1670370502.
# Баг это селениума или хрома выяснить не удалось.
#
# Из этой ситуации я нашёл 1 выход, возможно есть и другие способы решения этой проблемы. Преобразовать полученное
# значение expiry при помощи модуля time, передать в метод.strftime() формат даты'%Y-%m-%d' который соответствует
# формату ГОД-МЕСЯЦ-ДЕНЬ и передать в метод .localtime() время экспирации полученные с сайта.
#
# примерно вот так:  time.strftime('%Y-%m-%d', time.localtime(x['expiry']))
#
# И в таком случае мы получаем время экспирации в таком удобочитаемом виде с которым мы может работать и находить самое
# большое значение. ps. Если то что написано кажется слишком сложным, напишите в комментариях скину пример кода в лс.

# Siarhei R 9 дней назад

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/methods/5/index.html')
    max_exp, max_cookie_result = 0, 0
    for link in [element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, 'a')]:
        driver.get(link)
        max_exp_link = max(driver.get_cookies(), key=lambda x: x['expiry'])['expiry']
        if max_exp_link > max_exp:
            max_exp = max_exp_link
            max_cookie_result = driver.find_element(By.ID, 'result').text
    print(max_cookie_result)
# >563244506345412334251234560541

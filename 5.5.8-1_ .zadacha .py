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

# Павел Хошев в прошлом году
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    tmp = [i.get_attribute('href') for i in browser.find_elements(By.TAG_NAME, "a")]
    res = []
    for i in tmp:
        browser.get(i)
        code = browser.find_element(By.ID, 'result').text
        cook = browser.get_cookies()
        [print(time.strftime('%Y-%m-%d', time.localtime(x['expiry']))) for x in browser.get_cookies()]
        print(code,i)
        for x in cook:
            res.append({
                'expiry': [x['expiry'] for x in browser.get_cookies()],
                'code': code,
            })
    print(int(sorted(res, key=lambda x: x['expiry'], reverse=True)[0]['code']))
# >563244506345412334251234560541

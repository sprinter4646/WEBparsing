# https://stepik.org/lesson/720527/step/10?unit=721524

# Zadacha
# У вас есть список сайтов, 6 шт;
# На каждом сайте есть chekbox, нажав на этот chekbox появится код;
# Ваша задача написать скрипт, который открывает при помощи Selenium все сайты во вкладках (.window_handles);
# Проходит в цикле по каждой вкладке, нажимает на chekbox и сохранеят код;
# Из каждого числа, необходимо извлечь корень, функцией sqrt();
# Суммировать получившиеся корни и вставить результат в поле для ответа.
# ps. Верный ответ содержит  9 знаков после запятой, т.е имеет вид 000000.000000000,
# для округления используйте функцию round()
#
# psps. Рекомендую не пытаться обманывать, и извлекать числа другими способами. Работа с вкладками это одна из важных
# тем, которую необходимо освоить.
#

import time
from math import sqrt

from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html', ]

with webdriver.Chrome() as browser:
    answer = 0
    for n, site in enumerate(sites):
        n += 1
        browser.execute_script(f'window.open("{site}", "_blank{n}");')
        browser.switch_to.window(browser.window_handles[n])
        browser.find_element(By.CLASS_NAME, 'check_box').click()
        res = int(browser.find_element(By.CLASS_NAME, 'res').text)
        answer += sqrt(res)
    print(round(answer, 9))

# >>>334703.720482347

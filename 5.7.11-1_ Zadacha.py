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

# Павел Хошев в прошлом году
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []
with webdriver.Chrome() as browser:
    for x in range(1, 7):
        blank = browser.execute_script(f'window.open("http://parsinger.ru/blank/1/{x}.html", "_blank{x}");')
    tabs = browser.window_handles
    for z in range(len(tabs) - 1):
        if not browser.execute_script("return document.title;"):
            browser.close()
        browser.switch_to.window(browser.window_handles[z])
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        result.append(math.sqrt(int(browser.find_element(By.ID, 'result').text)))

print(sum(result))
# >>>334703.720482347

# https://stepik.org/lesson/715954/step/9?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/scroll/2/index.html с помощью Selenium;
# На сайте есть 100 чекбоксов, 25 из них вернут число;
# Ваша задача суммировать все появившиеся числа;
# Отправить получившийся результат в поля ответа.

# Павел Хошев в прошлом году
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/2/')

    for tag_input in browser.find_elements(By.TAG_NAME, 'input'):
        tag_input.click()

    for x in browser.find_elements(By.TAG_NAME, 'span'):
        if x.text.isdigit():
            result.append(int(x.text))
print(sum(result))

# >>>13310

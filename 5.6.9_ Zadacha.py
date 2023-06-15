# https://stepik.org/lesson/715954/step/9?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/scroll/2/index.html с помощью Selenium;
# На сайте есть 100 чекбоксов, 25 из них вернут число;
# Ваша задача суммировать все появившиеся числа;
# Отправить получившийся результат в поля ответа.
import time
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/2/index.html')
    answer = 0
    while True:
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
        for tag_input in input_tags:
            tag_input.send_keys(Keys.DOWN)
            tag_input.click()
            time.sleep(1)
        tag_al3last = browser.find_elements(By.TAG_NAME, 'p')
        for t in tag_al3last:
            if t.text[-3:].isdigit():
                print(t.text[-3])
                answer += int(t.text[-3:])
        print(answer)

# >>>13310

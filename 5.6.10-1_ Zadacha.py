# https://stepik.org/lesson/715954/step/10?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/scroll/3/ с помощью Selenium;
# Ваша задача, получить числовое значение  id="число" с каждого тега <input> который при нажатии вернул число;
# Суммируйте все значения и отправьте результат в поле ниже.
#
# На целевом сайте 500 тегов. Чтобы сэкономить вам время, мы позаботились о мини версии сайта, на нём всего 10 тегов.
# При правильном решении задачи, на тестовом сайте=http://parsinger.ru/scroll/training_task_3/ получившийся результат
# будет равен 18
# В этой задаче необходимо суммировать числа которые находятся в ID="число", если при нажатии на чекбокс появляется
# число в конце строки. На  тестовом сайте это числа 1,7,10
# Павел Хошев в прошлом году
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

result = []
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/3/')

    tag_input = browser.find_elements(By.TAG_NAME, 'input')
    tag_span = browser.find_elements(By.TAG_NAME, 'span')

    for ti, ts in zip(tag_input, tag_span):
        ti.send_keys(Keys.DOWN)
        ti.click()
        if ts.text:
            result.append(int(ti.get_attribute('id')))

print(sum(result))

# >>>9906

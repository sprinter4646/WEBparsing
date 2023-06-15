# https://stepik.org/lesson/709437/step/9?unit=710000
# Откройте сайт=http://parsinger.ru/selenium/3/3.html;
# Извлеките данные из каждого тега <p>;
# Сложите все значения, их всего 300 шт;
# Напишите получившийся результат в поле ниже.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    tags_p = browser.find_elements(By.TAG_NAME, 'p')
    print(sum([int(x.text) for x in tags_p]))

# >>> 450384194300

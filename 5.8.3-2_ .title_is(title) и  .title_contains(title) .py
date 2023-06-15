# https://stepik.org/lesson/715955/step/3?unit=716749

# .title_is(title) и  .title_contains(title)
# .title_contains(title)
# Синтаксис: WebDriverWait(browser, 5).until(EC.title_contains('tle'))
#
# То же самое, что и предыдущий код, только вернет True если title совпадает частично. Запустите код и поймите разницу,
# измените часть заголовка чтобы лучше понять разницу.

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    element = WebDriverWait(browser, 10).until(EC.title_contains('tle'))
    print(element)

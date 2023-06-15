# https://stepik.org/lesson/715955/step/3?unit=716749

# .title_is(title) и  .title_contains(title)
# Синтаксис: WebDriverWait(browser, 5).until(EC.title_is('title changed'))
#
# .title_is(title)
# title_is(title) - ожидание проверки заголовка страницы. title - ожидаемый заголовок, который должен быть точным
# совпадением, возвращает True, если заголовок совпадает, в противном случае, будет вы получите ошибку ->
#
# selenium.common.exceptions.TimeoutException: Message:
# Откройте сайт=http://parsinger.ru/expectations/2/index.html и нажмите кнопку на странице, обратите внимание на
# заголовок. Запустите код ниже у себя в терминале,  чтобы посмотреть как он работает. Этот код ожидает 10 секунд, пока
# заголовок не станет "title changed",  когда заголовок полностью совпадет, код вернет True

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    element = WebDriverWait(browser, 10).until(EC.title_is('title changed'))
    print(element)

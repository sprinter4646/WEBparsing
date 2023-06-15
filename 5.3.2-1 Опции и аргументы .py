# https://stepik.org/lesson/716118/step/2?auth=login&unit=716910
# Запуск браузера в скрытом режиме
# Запуск браузера в фоновом режиме, очень прост, достаточно запомнить всего один параметр и синтаксис. Для этого нам
# потребуется метод  .add_argument() и передать ему параметр --headless. Для примера откроем первую страницу Яндекса,
# и получим первую найденную ссылку.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--disable-gpu')  # То ли я, что то не так делаю, то ли проблема в Убунту,
# но --headless на моем линуксе не работает. А вот --disable-gpu сработал. Спасибо, что и его указали

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(50)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))

# >>> https://passport.yandex.ru/auth?origin=home_yandexid&retpath=https%3A%2F%2Fyandex.ru&backpath=https%3A%2F%2Fyandex.ru
# https://www.ya.ru/
# Преимущества запуска браузера в фоновом режиме.
#
# Отсутствует отрисовка содержимого, тем самым потребляется меньше ресурсов.
# Работает быстрее, т.к. не нужно ничего отрисовывать) Использование --headless может значительно ускорить работу
# парсера на относительно слабых машинах.
# Не занимает место на экране, и не мешает вашей работе во время выполнения скрипта.
# В некоторых гайдах вы можете встретить параметр --disable-gpu, который по сути, выполняет то же самое что и --headless
# - запускает браузер "без головы".

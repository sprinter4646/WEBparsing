# https://stepik.org/lesson/716118/step/1?auth=login&unit=716910
# В папке появится файл "coordinates.crx", это и есть наше упакованное расширение, теперь оно готово к использованию.
# Осталось "скормить" его в Selenium.
# В этом примере я переименовал файл 0.2_0.crx => coordinates.crx
import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(50)

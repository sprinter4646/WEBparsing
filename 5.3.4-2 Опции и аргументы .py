# https://stepik.org/lesson/716118/step/4?auth=login&unit=716910
# Proxy и Selenium
# Теперь модифицируем данный код, чтобы запрос отправлялся через прокси.
#
# Прокси должен быть вида IP:PORT
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# PROXY = '45.10.81.217:8000'  # с купленным proxy = '45.10.81.217:8000:GVFJNw:yneWoN' работает!
PROXY = "GVFJNw:yneWoN@45.10.81.217:8000"
url = 'https://2ip.ru/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(url)
    time.sleep(50)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
# Первое, что мы сделали, - передали параметр '--proxy-server=%s' % proxy методу .add_argument() в класс дополнительных
# опций .ChromeOptions() и передали сам прокси, который лежал в переменной proxy. Если этот прокси еще живой, можете
# запустить этот код у себя в IDE. Если прокси умер, то с помощью скрипта в первом абзаце можете спарсить себе новый
# список.

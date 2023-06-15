# https://stepik.org/lesson/716118/step/2?auth=login&unit=716910
# Запуск браузера в скрытом режиме
# Если вам потребуется запустить браузер с расширениями  и в режиме --headless, то необходимо прописать
# options.add_argument("--headless=chrome")
#
# Код будет выглядеть примерно так:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')


options_chrome.add_argument('--disable-gpu==chrome')  # 4 месяца назад @Юрий_Верескун,  заменить строку
# options_chrome.add_argument('--headless=chrome') на строку options_chrome.add_argument(' --disable-gpu==chrome')
# будет в результате что то похожее на выполнение кода,  задуманное автором))

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(5)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))

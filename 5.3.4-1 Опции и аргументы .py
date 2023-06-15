# https://stepik.org/lesson/716118/step/4?auth=login&unit=716910
# Proxy и Selenium
# Работа с прокси в Selenium очень проста, намного проще, чем в requests, где мы создавали словарь, прописывали в ключах
# схемы, и затем передавали его в запросе.
#
# Мы можем узнать свой IP на сайте 2ip.ru=https://2ip.ru/.
# Выполните код ниже, чтобы увидеть к принт в консоли с вашим IP адресом.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://2ip.ru/'
with webdriver.Chrome() as browser:
    browser.get(url)
    # в первом блоке кода нужно поменять местами последнюю и предпоследнюю строку.
    # sleep нужен, чтобы подождать загрузки основной страницы, и потом забрать с нее информацию по указанию на элемент.
    # в текущей реализации происходит попытка забрать элемент до того, как загрузится страница и выдается ошибка.
    time.sleep(5)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

# >>> 171.33.254.215

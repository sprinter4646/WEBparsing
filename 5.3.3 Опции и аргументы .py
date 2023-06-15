# https://stepik.org/lesson/716118/step/3?auth=login&unit=716910
# Перенос профиля с основного браузера Chrome в браузер под управлением Selenium
# Вы можете захотеть перенести все настройки, закладки, историю с основного браузера, в браузер под управлением
# Selenium. Сейчас я вам покажу, как это можно сделать.
#
# Определяем путь к папке с профилями \User Data\, для этого напишите команду, в адресной строке браузера
# chrome://version/  и ищите адрес в поле с заголовком "Путь к профилю:" У меня адрес выглядит вот так:
# C:\Users\user\AppData\Local\Google\Chrome\User Data\
# 'user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data' добавьте путь к профилю в метод
# .add_argument()
import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
# в прошлом месяце
# Если вдруг кто не может запустить основной профиль в Chromium на убунте, мне помогло следующее изменение пути:
# options_chrome.add_argument("user-data-dir=/home/oleg/.config/google-chrome"), где username - имя вашего профиля,
# вместо user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data'
options_chrome.add_argument('user-data-dir=/home/oleg/.config/google-chrome')  # заменил chromium на google-chrome
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(100)

# Если все сделано правильно, то у вас запустится окно браузера с вашими параметрами, историей, закладками.
#
# Если у вас возникает ошибка "invalid argument: user data directory is already in use, please specify
# a unique value for", значит, данный профиль уже используется. Закройте основной браузер и повторите попытку.
# Если вам необходимо основное окно браузера, то скопируйте полностью папку  \User Data\ в удобное место
# и укажите путь к ней.

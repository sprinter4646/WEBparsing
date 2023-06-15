# https://stepik.org/lesson/705985/step/1?auth=login&unit=706437
# Скопируйте код, ниже и запустите у себя в IDE, если окно браузера открылось и там загрузился stepik.org то
# поздравляю вас, установка выполнена успешна. Если код ниже не заработал, перезагрузите компьютер.
import time
from selenium import webdriver

url = 'https://stepik.org'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(50)

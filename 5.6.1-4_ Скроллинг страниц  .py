# https://stepik.org/lesson/715954/step/1?unit=716748

# 5.6 Скроллинг страниц
# Прокрутка содержимого страницы - способ 1 execute_script()
# Для того, чтобы вычислить высоту видимой области сайта, используется скрипт #
# Используется код window.innerHeight для получения высоты или  window.innerWidth - для получения ширины видимой области
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    height = browser.execute_script("return window.innerHeight")
    print(height)

# >>> 806
# 806 пикселей имеет видимая часть нашего сайта. Иногда необходимо, чтобы требуемый элемент находился в видимой области,
# т.к. методы .click(), .send_keys() и др. не могут быть совершены, если элемент не находится в видимой области экрана.

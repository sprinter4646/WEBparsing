# https://stepik.org/lesson/715954/step/1?unit=716748

# 5.6 Скроллинг страниц
# Прокрутка содержимого страницы - способ 1 execute_script()
# Если вам необходимо совершить скроллинг в самый низ к последнему пикселю одним из самых простых способов, то
# используйте скрипт  "window.scrollTo(0,document.body.scrollHeight)"
import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
# При написании парсеров, часто необходимо сперва совершить необходимое количество скроллинга, чтобы загрузилась вся
# необходимая вам информация. После того как вся  нужная инфа появилась на странице, мы собираем всё при помощи
# .find_elements(), но об этом мы будем говорить далее.

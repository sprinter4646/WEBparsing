# https://stepik.org/lesson/720527/step/9?unit=721524

# Вкладки в браузере
# Получаем title вкладки
# title - это то, что содержится в HTML тегах  <title>Текст на вкладке</title> и то что отображается на вкладке
# браузера.
#
# Чтобы получить имя вкладки, т.е., ее title , используется метод .execute_script("return document.title;"), в который
# мы передали код Javascript, возвращющий имя вкладки.
#
# Запустите код ниже, у себя в терминале. Этот код откроет степик, и напечатает вам в консоли title вкладки.

from selenium import webdriver
with webdriver.Chrome() as browser:
    browser.get("https://stepik.org/course/104774/promo")
    print(browser.execute_script("return document.title;"))


# >>> WEB Парсинг на Python — Stepik


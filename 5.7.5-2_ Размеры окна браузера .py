# https://stepik.org/lesson/720527/step/4?unit=721524

# ZРазмеры окна браузера
# .get_window_size()
# Для получения размеров окна браузера используется метод .get_window_size(), у него есть метод .get(),  который
# принимает 2 параметра 'height' и 'width' соответственно, они возвращают высоту и ширину окна браузера.
from selenium import webdriver
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    browser.set_window_size(1200, 720)
    print(browser.get_window_size().get('height'))
    print(browser.get_window_size().get('width'))
    # При вызове метода .get_window_size() в ответ мы получим словарь, который содержит ширину и высоту окна браузера.
    print(browser.get_window_size())
    # Как и при работе с любым словарем, мы можем получить доступ к ширине или высоте по ключу ["width"] и  ["height"]
    print(browser.get_window_size()['height'])
    print(browser.get_window_size()['width'])
# >>> 720
# 1200
# {'width': 1200, 'height': 720}
# 720
# 1200

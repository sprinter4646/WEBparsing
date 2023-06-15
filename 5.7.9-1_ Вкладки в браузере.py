# https://stepik.org/lesson/720527/step/9?unit=721524

# Вкладки в браузере
# При работе в браузере, мы можем открывать новые вкладки и работать в них. Мы можем открыть любое количество вкладок
# одновременно, но работать мы можем только в активной. Мы можем переключаться между вкладками, получить их title,
# проходить по вкладкам в цикле, получить их дескрипторы, практически все то, что вы делаете вручную.
#
# Вам может понадобится собрать данные со второй вкладки, не отвлекаясь на первую. Или сайт, который вы парсите ,
# открывает ссылки в новой вкладке, такое происходит если у ссылок есть атрибут  target="_blank".
#
# Дескриптор - это идентификатор вкладки браузера, в Opera и Chrome дескрипторы выглядят одинаково,
# CDwindow-8696D8A3F222B281BB03FC1EC259B251,
# а в Firefox они выглядят немного иначе,
# d8e0e954-bf72-4eae-a63e-5ea404c3b0eb.
# Дескрипторы - это те сущности, которые помогают нам манипулировать вкладками.
#
# .current_window_handle - возвращает дескриптор текущей вкладки;
# .window_handles - возвращает список всех дескрипторов открытых вкладок;
# .switch_to.window(window_handles[0]) - переключает фокус между вкладками.
# Запустите код ниже, чтобы посмотреть, как он работает. Этот код открывает первую вкладку методом .get("URL"), далее,
# открывает ещё три вкладки методом  .execute_script(), и в после этого печатает все дескрипторы открытых вкладок.

import time
from selenium import webdriver
with webdriver.Chrome() as browser:
    result = []
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(3)
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
    time.sleep(2)
    print(browser.window_handles)

# >>> ['CDwindow-FB580151A416179D7204A36722F50B18', 'CDwindow-12E90DEA6DFEE366B620282C8A228131',
# 'CDwindow-92FEA4784AB5E877CE8ADCF42D1FB1DE', 'CDwindow-75AB8AC2EFB6B091AC149C007E9B787B',
# 'CDwindow-F69371F46370168A1F355842C8F4A4AD']

# НИФИГА
# >>> ['5BA523995600A04A77F02551771CBBF6', '64405A2C60319FE34D4E8DD134E16599', 'DC74CE98C44E6B26AA14E5BA90F6702D',
# 'CCCE4C921F33BBFCD3A082FA43799185']


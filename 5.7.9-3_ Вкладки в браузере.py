# https://stepik.org/lesson/720527/step/9?unit=721524

# Вкладки в браузере
# Чтобы лучше понять, как происходит итерирование по вкладкам, я создал следующий пример. Запустите код ниже у себя в
# терминале и посмотрите, как происходит итерирование. Также обратите внимание на то, что вкладка с именем data не
# возвращает своего имени, т.к. не содержит тега <title>.

import time
from selenium import webdriver
with webdriver.Chrome() as browser:
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        print(browser.execute_script("return document.title;"), browser.window_handles[x])
# >>>FB0F2D9D4D0C37FD70112EE3929A2ACF
# 5 0A33E0BB986A55094F079EC2BF42899B
# 1 E225D1E0ED9765F69EFB03D9EB3A0B43
# 4 F13A486528923149B56F1B7C81007E2E
# 3 E440C36E8B5269B4E26490CF3B894120
# 6 F80B449DCD9E494D9155E74A31E28DA0
# 2 821ED825878687078C09EE2A5528E082

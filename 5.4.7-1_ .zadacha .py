# https://stepik.org/lesson/709437/step/7?unit=710000
# Самое время выполнить простую задачку для закрепления пройденного материала.
#
# Суть задачи проста( у вас будет всего 5 секунд для того чтобы получить результат, поэтому подумайте над кодом)
#
# Открыть сайт=http://parsinger.ru/selenium/1/1.html с помощью selenium;
# Заполнить все существующие поля;
# Нажмите на кнопку;
# Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд;
# Вставьте результат в поле ниже.
# Для заполнения полей вам потребуется метод .send_keys("Текст"), который мы применяем к каждому полю input,
# помните про универсальный метод .find_elements(), который возвращает список найденных элементов. Используйте этот
# метод для поиска всех полей.
# Евгений Жужук в прошлом году
# Решил сделать все автоматически - получить имена тегов и ими же заполнить форму, нажать кнопку, получить секретный код
# и вывести принтом.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://stepik-parsing.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    list_names = browser.find_elements(By.TAG_NAME, 'input')
    for form, text in zip(input_forms, list_names):
        form.send_keys(text.get_attribute("name"))
    button = browser.find_element(By.ID, "btn").click()
    secret_code = browser.find_element(By.ID, 'result').text
    print(secret_code)
    time.sleep(10)
# Для решения задачи используйте цикл,  чтобы обойти найденные элементы, методом .find_elements(), и на каждой итерации
# к каждому полю применяйте метод .send_keys("text") для его заполнения, а метод .click() используйте чтобы нажать
# на кнопку. Не забудьте про модуль time чтобы установить задержки.


# https://stepik.org/lesson/715954/step/10?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/infiniti_scroll_1/ с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
# Используйте Keys.DOWN или .move_to_element();
# Цель: получить все значение в элементах, сложить их;
# Получившийся результат вставить в поле ответа.
# Подсказка:
# Элементы могут грузится медленнее чем работает ваш код, установите задержки.
# Подумайте над условием прерывания цикла, последний элемент в списке имеет class="last-of-list"


# Павел Хошев в прошлом году
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/infiniti_scroll_1/'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(0.5)
    count = 0
    checking = []
    result = []
    while True:
        input_list = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]

        for inp in input_list:
            if inp not in checking:
                inp.send_keys(Keys.DOWN)
                count += 1
                checking.append(inp)

        break_loop = [x for x in browser.find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
        if break_loop:
            break
    span_list = [result.append(int(x.text)) for x in
                 browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]
    print(f'Результат: {sum(result)}')
# >>> 86049950

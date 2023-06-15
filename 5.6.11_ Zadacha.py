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

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

res_0 = 9050
res_10 = 900500
result = 0
for n in range(0, 100):
    if n < 10:
        res = res_0 + (n * 100) + n
    else:
        res = res_10 + (n * 1000) + n
    result += res
    print(res)
print(result)
# >>> 86049950

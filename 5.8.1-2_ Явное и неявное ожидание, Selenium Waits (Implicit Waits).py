# https://stepik.org/lesson/715955/step/1?unit=716749

# Явное и неявное ожидание, Selenium Waits (Implicit Waits)
# Давайте немного модифицируем код выше, чтобы он работал без ошибок. Применим неявные ожидания. О том, как они
# работают, мы поговорим в следующих степах и порешаем задачки по ним.
#
# Больше инфы по этим ссылкам:
# ссылка=https://selenium-python.readthedocs.io/waits.html,
# ссылка=https://www.selenium.dev/documentation/webdriver/waits/ и
# ссылка=https://habr.com/ru/post/273089/.
# Запустите эти два примера у себя в IDE, чтобы сравнить результат работы.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    print(browser.find_element(By.ID, 'result').text)

# Коротко опишу то, что тут произошло:
#
# Импортировали модуль expected_conditions из библиотеки webdriver и назвали его EC, чтобы не писать каждый раз его
# длинное название;
# Импортировали сам класс для работы с ожиданиями WebDriverWait;
# Использовали функцию element_to_be_clickable, которая ожидает пока элемент станет кликабельным;
# Как только элемент стал кликальбельным, управление программой передается далее, и метод
# browser.find_element(By.ID, 'btn').click() и совершается клик по элементу.

# Теперь чуть подробнее:
#
# element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn")))
#
# element = WebDriverWait(browser, 10) - создали экземпляр класса WebDriverWait, передав в него объект вебдрайвера
# browser, где число 10 - это время, в течение которого мы ждем, пока элемент станет кликабельным, проверка элемента
# происходит каждые 0.5 секунды, параметр poll_frequency=0.5 может как уменьшить время опроса, так и увеличить;
# .until(EC.element_to_be_clickable((By.ID, "btn") -  к созданному экземпляру класса element применили функцию until,
# которая непосредственно и выполняет всю работу. К этой функции мы применили метод element_to_be_clickable, который
# проверяет на кликабельность переданный ему элемент, и потом функция .click() совершает клик в нужный момент.


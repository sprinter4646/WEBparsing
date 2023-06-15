# https://stepik.org/lesson/715954/step/6?unit=716748

# Прокрутка содержимого страницы - способ 3 ActionChains()
# ActionChains() - цепочка действий, это способ автоматизации низкоуровневых взаимодействий, таких как движения мыши,
# действия кнопок мыши, нажатие клавиш и взаимодействие с контекстным меню.
#
# Импортируем:  from selenium.webdriver.common.action_chains import ActionChains
#
# Когда вы вызываете методы для действий в объекте ActionChains, действия сохраняются в очереди в объекте ActionChains.
# Когда вы вызываете .perform(), события запускаются в том порядке, в котором они стоят в очереди.
#
# ActionChains(webdriver) - принимает единственный объект, объект webdriver'a.
#
# .perform() - выполняет запуск цепочки действий, написание этого метода в конце каждой цепочки , просто необходимо для
# его запуска.
#
# menu = driver.find_element(By.CSS_SELECTOR, ".nav")
# hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
#
# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
# Когда мы пишем код, мы можем синтаксически разрывать цепочку, ведь каждое написанное действие хранится в очереди
# объекта ActionChains.
#
# menu = driver.find_element(By.CSS_SELECTOR, ".nav")
# hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
#
# action = ActionChains(driver)
# time.sleep(1)
# action.move_to_element(menu)
# time.sleep(1)
# action.click(hidden_submenu)
# time.sleep(1)
# action.perform()
# Для примера, чтобы переместиться к определенному элементу и кликнуть по нему, мы напишем следующий код
from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     target = browser.find_element(By.ID, 'like')
#     actions = ActionChains(browser).move_to_element(target).click().perform()
#     Обратите внимание, что методу .move_to_element() необходимо указать цель, целью служит любой интерактивный элемент
#     на странице, кнопка, ссылка, форма и т.д. Об остальных методах мы поговорим в следующем степе, а пока покажу, как
#     тот же самый код написать более гибким способом.
# import time
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# with webdriver.Chrome() as browser:
#     target = browser.find_element(By.ID, 'like')
#     actions = ActionChains(browser)
#     "тут может находится любой код, от time.sleep() до перехода в новую вкладку и т.д"
#     actions.move_to_element(target)
#     "тут может находится любой код, от time.sleep() до перехода в новую вкладку и т.д"
#     actions.click()
#     "тут может находится любой код, от time.sleep() до перехода в новую вкладку и т.д"
#     actions.perform()

# Наталья Попова 9 месяцев назад непонятно без живого примера
# Павел Хошев 9 месяцев назад
# @Наталья_Попова, В этом примере цикл while запускает бесконечный цикл для  scroll, а в scroll мы передаём координаты
# расположения скролящегося окна. Пример не идеален т.к. нет условия прерывания бесконечного цикла, это условие нужно
# придумать для каждой ситуации своё.

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    while True:
        ActionChains(browser).scroll_from_origin(0, 250, 700).perform()



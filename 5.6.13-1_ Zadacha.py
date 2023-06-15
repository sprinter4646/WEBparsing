# https://stepik.org/lesson/715954/step/13?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/infiniti_scroll_3/ с помощью Selenium
# На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100 элементов;
# Необходимо прокрутить все окна в самый низ;
# Цель: получить все значение в каждом из окошек и сложить их;
# Получившийся результат вставить в поле ответа.

# Павел Хошев в прошлом году
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


start = time.time()
url = 'http://parsinger.ru/infiniti_scroll_3/'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('coordinates.crx')
result = []

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get(url)
    browser.set_window_size(1024, 720)

    while True:
        ActionChains(browser).scroll(85, 275, 85, 275).perform()
        ActionChains(browser).scroll(280, 300, 280, 300).perform()
        ActionChains(browser).scroll(480, 300, 480, 300).perform()
        ActionChains(browser).scroll(680, 320, 680, 320).perform()
        ActionChains(browser).scroll(900, 300, 900, 300).perform()

        catch_last_elem = [x for x in browser.find_element(By.ID, 'scroll-container_5').find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
        if catch_last_elem:
            [result.append(int(x.text)) for x in browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'span')]
            break

print(sum(result))
print(f'Time is running{time.time() - start}')
# >>>159858750

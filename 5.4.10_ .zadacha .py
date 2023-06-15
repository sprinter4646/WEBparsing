# https://stepik.org/lesson/709437/step/10?unit=710000
# Откройте сайт=http://parsinger.ru/selenium/3/3.html;
# Извлеките данные из каждого  второго тега <p>;
# Сложите все значения, их всего 100 шт;
# Напишите получившийся результат в поле ответа.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    # tags_p = browser.find_elements(By.TAG_NAME, 'p')
    tags_p = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    print(sum([int(x.text) for x in tags_p]))

# .find_elements(By.XPATH, "//div[@class='text']/p[2]") - соответственно, вернёт все найденные элементы <p>,
# <div class="text">
# 			<p>191817</p>
# 			<p>121314</p>
# 			<p>151715</p>
# 		</div>
# расположенные на вторых позициях, во всех найденных <div class="text">.

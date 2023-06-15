# https://stepik.org/lesson/709437/step/4?unit=710000
# Работаем с браузером
# Когда наш парсер отработает, мы бы хотели, чтобы он закрылся сам и тем самым корректно завершил свою работу.
# Но этого может не произойти по множеству причин. Поэтому мы должны указать браузеру на то, что он должен закрыть окно
# после завершения работы командой browser .quit(). Важно закрывать окно, потому что при создании webdriver.Chrome()
# создается процесс в OC, который продолжит висеть. Команда .quit() проще, чем закрывать окно браузера вручную, к тому
# же вы не будете засорять оперативную память.
#
# Расставим таймауты, чтобы видеть процесс выполнения кода и чтобы браузер не закрывался за мгновение.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button")
time.sleep(2)
button.click()
time.sleep(2)
browser.quit()

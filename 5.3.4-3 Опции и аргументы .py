# https://stepik.org/lesson/716118/step/4?auth=login&unit=716910
# Proxy и Selenium
# Если прокси умер, то с помощью скрипта в первом абзаце можете спарсить себе новый список.
# Подобно requests,  мы можем установить timeout= для загрузки страницы, после истечению которого произойдет,
# либо закрытие окна, либо переход к следующему прокси.

from selenium import webdriver
from selenium.webdriver.common.by import By

proxy_list = '45.10.81.217:8000',


for PROXY in proxy_list:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        url = 'https://2ip.ru/'

        with webdriver.Chrome(options=chrome_options) as browser:
            browser.get(url)
            print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

            browser.set_page_load_timeout(10)

            proxy_list.remove(PROXY)
    except Exception as _ex:
        print(f"Превышен timeout ожидания для - {PROXY}")
        continue
# >>> Превышен timeout ожидания для - 8.210.83.33:80
# >>> Превышен timeout ожидания для - 199.60.103.28:80
# >>> Превышен timeout ожидания для - 103.151.246.38:10001
# >>> Превышен timeout ожидания для - 199.60.103.228:80
# >>> Превышен timeout ожидания для - 199.60.103.228:80
# >>> Превышен timeout ожидания для - 199.60.103.28:80
# Так понимаю это список нерабочих IP адресов

# https://stepik.org/lesson/716118/step/4?auth=login&unit=716910
# Proxy и Selenium
# Proxy with authorization
# Proxy с авторизацией
# Нашел вот такой рабочий вариант работы с прокси
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "45.10.81.217:8000"  # "ip_addr:port"
prox.socks_proxy = "45.10.81.217:8000"
prox.ssl_proxy = "45.10.81.217:8000"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)

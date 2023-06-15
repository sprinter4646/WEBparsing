# https://stepik.org/lesson/691440/step/4?unit=690987
# Используйте hidemy.name, чтобы скачать 10шт бесплатных прокси. И сохраните их в файл с именем proxy.txt
# Прокси proxies=
# Библиотека Requests позволяет отправлять запросы, скрывая свой настоящий IP-адрес. Зачем его скрывать? Например,
# потому что очень часто за высокочастотные запросы можно получить бан.
import time
import requests

url = 'http://httpbin.org/ip'
proxy = {
    'http': 'http://45.10.81.217:8000',
    'https': 'https://45.10.81.217:8000',

}

# response = requests.get(url=url, proxies=proxy)
# print(response.json())

# --------------------------------------
# Для socks4
proxy_socks4 = {
    'http': 'socks4://45.10.81.217:8000',
    'https': 'socks4://45.10.81.217:8000',

}

# --------------------------------------
# Для всех, с авторизацией
proxy_all_auth = {
    'http': "socks5://GVFJNw:yneWoN@45.10.81.217:8000",
    'https': "socks5://GVFJNw:yneWoN@45.10.81.217:8000",
}

response = requests.get(url=url, proxies=proxy_all_auth)  # , proxies=proxy_socks4
time.sleep(1)
print(response.json(), 'Success connection')

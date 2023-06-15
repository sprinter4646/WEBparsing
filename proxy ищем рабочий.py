# https://stepik.org/lesson/691440/step/4?unit=690987
import requests

url = 'http://httpbin.org/ip'  # "origin": "171.33.254.215"
proxy = {
    'http': 'http://103.177.45.3:80',
    'https': 'https://103.177.45.3:80',

}

response = requests.get(url=url, proxies=proxy)
print(response.json())

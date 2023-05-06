# https://stepik.org/lesson/724024/step/1?unit=725138
# Если вы скопируете ссылку=https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0,
# которая находится в левой части на скриншоте выше, вы получите ошибку
# "Страница bitality.cc не найдена". Так происходит потому, что мы совершаем прямой запрос к серверу, где лежат данные,
# но мы не передаем ключ 'x-requested-with': 'XMLHttpRequest'.
#
# Давайте напишем скрипт и передадим с запросом ключ requested-with': 'XMLHttpRequest' и стандартный юзер-агент.
import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

# url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
url = "https://enter-change.com/Home/ClientAction?param=TrgFhz&GiveName=Bitcoin&GetName=Tether%20TRC-20&Sum=0.10628374&Direction=0"
response = requests.get(url=url, headers=headers).json()
print(response)
# >>> {'giveSum': '4.1895414', 'getSum': '0.25619551'}
# >>>{'giveSum': 0.10628374, 'getSum': '3103.74721057'}

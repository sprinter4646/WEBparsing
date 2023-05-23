# https://stepik.org/lesson/704700/step/2?auth=login&unit=705135
# Парсим JSON часть 2
# Для того, чтобы получить все 'userId' и 'title', мы пройдемся по всем элементам в цикле for:
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url).json()
for item in response:
    print(item["userId"], item["title"])

# >>> 1 sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# 1 qui est esse
# 1 ea molestias quasi exercitationem repellat qui ipsa sit aut
# 1 eum et est occaecati
# ....
# 10 at nam consequatur ea labore ea harum
# В результате мы получили все  "userId" и "title". Обратите внимание на применяемый к response метод .json(),
# мы говорили об этом в разделе, посвященном requests. Этот метод помогает сериализовать данные с сервера в JSON-объект,
# при условии, что сервер готов нам их отдать.

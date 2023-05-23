# https://stepik.org/lesson/704700/step/2?auth=login&unit=705135
# Парсим JSON часть 2
# Вложенность JSON
# Для следующего примера нам понадобится результат выполнения одной из прошлых задач.
# Для удобства вы можете найти его по ссылке=https://parsinger.ru/downloads/get_json/res.json.
#
# Наша цель -  извлечь из значения ключа "description" вложенные ключи "brand" и "model". Для этого первым ключом
# указывается родительский элемент, а после дочерний ["description"]["brand"]:
import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
for item in response:
    print(item["description"]["brand"], item["description"]["model"])

# >>> Jet Excidium
# Huawei Band 6 FRA-B19
# Huawei Band 6 FRA-B19
# ...
# HP Pavilion Gaming 600

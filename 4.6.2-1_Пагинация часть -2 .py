# https://stepik.org/lesson/700334/step/2?unit=700275
# Пагинация часть -2
# Часто бывает, что мы не можем получить все ссылки из пагинации и нам приходится генерировать их самостоятельно.
# Звучит странно, но вы сейчас поймете, о чем я.
#
# Для примера посмотрим на ссылку маркета www.wildberries.ru
# wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page=8
# Самые догадливые, надеюсь, уже поняли, что мы будем делать дальше. Правильно, генерировать ссылки.
# Делается это при помощи f'' строки.
link = []
for i in range(1, 101):
    link.append(f'https://www.wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page={i}')
print(link)
# >>> ['https://www.wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page=1',
#      'https://www.wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page=2',
#        ..............
#      'https://www.wildberries.ru/catalog/elektronika/smart-chasy?sort=popular&page=100']


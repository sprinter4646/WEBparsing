# https://stepik.org/lesson/701336/step/1?unit=701405
# CSV
# Работа с модулем CSV очень проста, и нам понадобится запомнить лишь пару приемов для того,
# чтобы успешно применять его на практике.
# Для начала, нам нужно знать что любой список легко превратить в CSV
# lst = ['one', 'two', 'three'] >>> 'one', 'two', 'three'
import csv

lst = ['one', 'two', 'three']

with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(lst)
# Чтобы в Excel корректно открывалась кодировка, используйте encoding='utf-8-sig'.
# В результате выполнения этого кода будет создан файл res.csv, в который будет записан наш список lst,
# в каждой ячейке - элемент списка.
#
# newline='' - необходимо указывать всегда. Если не указать, то новые строки могут интерпретироваться  неправильно
# и весь документ “сползет”;
# encoding='utf-8-sig' - open() использует для открытия .csv  по умолчанию кодировку unicode. Чтобы получить файл с
# необходимой нам кодировкой, нужно явно указывать ее.
# writer = csv.writer(file, delimiter=';') - в этой строке мы создали экземпляр класса csv и применили к нему метод
# writer(). У writer() есть метод writerow(), с помощью которого можно записывать список в соответствующий формат
# построчно. delimiter=';' указывает, каким будет разделитель между элементами списка, мы можем указать любой.

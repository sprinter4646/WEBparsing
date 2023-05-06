# https://stepik.org/lesson/699724/step/1?unit=699646
# Чтобы приступить к анализу HTML кода, нам необходимо передать его в конструктор BeautifulSoup .
#
# Мы можем передать текстовый файл в формате HTML или объект response.text из библиотеки requests,
# о которой мы говорили ранее.
#
#  Передаём объект response.text
from bs4 import BeautifulSoup
import requests
import lxml

# Пример 3. Передача объекта response прямо из запроса
response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
# Этот пример используется чаще всего.  В этом примере мы совершили .get запрос, затем передали результат запроса
# в конструктор BeautifulSoup. Обратите внимание на метод .text, который мы применили к объекту response.
# Конструктор BeautifulSoup умеет работать только с HTML, именно поэтому мы преобразуем объект response в текст.
# Если этого не сделать, мы получим ошибку TypeError: object of type 'Response' has no len() , об этом важно знать.
# Если у вас во время запроса к данной странице возникли проблемы с кодировкой,  и вы видите нечто подобное
# <title>Ð£ÑÐ¸Ð¼ÑÑ Ð¿Ð°ÑÑÐ¸ÑÑ</title> ,
# необходимо применить метод response.encoding = 'utf-8', К сожалению, такое поведение иногда встречается,
# и я пока не знаю, как решить эту проблему на этом тренажере.

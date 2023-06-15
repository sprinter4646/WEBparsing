# https://stepik.org/lesson/709437/step/6?unit=710000
# .find_element()и find_elements()
# Методы .find_element()  и find_elements() вы будете использовать всегда при написании парсеров с помощью Selenium.
# Поэтому их нужно хорошо понимать.
#
# У нас есть сайт с очень простой структурой дерева HTML. На странице есть 100 блоков <div="text">, в каждом три
# тега <p>, которые не имеют ни class, ни id . Нам необходимо собрать каждый первый элемент <p>. Мы могли бы пройти в
# цикле и использовать срезы, как мы делаем с простыми списками, наверняка подумали вы.
# <div class="text">
#           <p>191817</p>
#           <p>121314</p>
#           <p>151715</p>
#           </div>
# Давайте разбираться, почему срезы не сработают.
#
# .find_element() вернет нам объект вебдрайвера, который не поддерживает срезы. Выполним следующий код:
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CLASS_NAME, 'text')
    print(type(link))

# >>> <class 'selenium.webdriver.remote.webelement.WebElement'>
# Мы видим, что возвращаемый тип объекта  - это экземпляр класса,  который содержит в себе список элементов <p>
# в количестве трех штук, как показано на первом скриншоте. Но это не простой список.
#
# Давайте посмотрим на возвращаемый объект.
    print(link)
# >>> <selenium.webdriver.remote.webelement.WebElement (session="a7cb2c979d456b7cae336e5eafa4ad6b",
# element="c2651e50-25a3-41bb-ad8d-5a259929bbfe")>
# Это элемент selenium, который не поддерживает срезы. Давайте попытаемся получить элемент [0] у этого объекта и
# посмотрим на результат.
    # print(link[0])
# >>> TypeError: 'WebElement' object is not subscriptable
# Получаем ошибку, которая подтверждает, что объект не может быть итерирован. Так происходит, потому что все элементы
# <p>, которые мы храним в этом объекте, являются как бы одним целым.
# А вот извлечь из этого объекта текст очень просто, достаточно применить к нему метод .text
    print(link.text)

# >>> 191817
#     121314
#     151715



# https://stepik.org/lesson/709437/step/6?unit=710000
# .find_element()и find_elements()
# .find_element() - Возвращает первый найденный элемент, соответствующий нашим критериям поиска, (имеется ввиду элемент
# веб-драйвера, который содержит внутри себя элемент/тег DOM )
#
#  .find_elements() -  Возвращает все найденные элементы, соответствующие критериям поиска и сохраняет результат в
#  список <class 'list'>, но список будет наполнен НЕ элементами <p>, а элементами веб драйвера, которые будут содержать
#  в себе элементы DOM.
#
#
#
# Как все-таки быть, если нам нужен каждый второй или третий элемент на странице ?
#
# Мы всегда можем решить эту задачу при помощи XPath.
# .find_element(By.XPATH, "//div[@class='text']/p[2]") - вернет нам второй элемент <p>, первого найденного элемента
# <div class="text">.
# .find_elements(By.XPATH, "//div[@class='text']/p[2]") - соответственно, вернёт все найденные элементы <p>,
# расположенные на вторых позициях, во всех найденных <div class="text">.
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    # link = browser.find_elements(By.CSS_SELECTOR, 'p:nth-child(2)')
    print(*[x.text for x in link], sep='\n')
    '''for el in link:
        print(el.text)'''


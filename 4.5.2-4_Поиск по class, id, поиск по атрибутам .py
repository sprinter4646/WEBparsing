# https://stepik.org/lesson/700231/step/4?unit=700173
# Как найти элемент/ы по классу ?
#
# Выберите все подходящие ответы из списка
# soup.find_all('class_', p='name')
# soup.find_all('p', class_='name')
# soup.find('p', class_='name')
# soup.find('p', clas_='name')
# soup.find('p', class='name')
# soup.find_all('p', class='name')

from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('p', class_='article').text
print(div)

#
# print(soup.find_all('class_', p='name'))    # soup.find('p', class='name')
print(soup.find_all('p', class_='name'))    # soup.find('p', class='name')
print(soup.find('p', class_='name'))        # soup.find('p', class_='name')
print(soup.find('p', clas_='name'))         # soup.find('p', clas_='name')
# print(soup.find('p', class='name'))       # soup.find('p', class='name')
# print(soup.find_all('p', class='name'))   # soup.find_all('p', class='name')

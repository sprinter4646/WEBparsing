# https://stepik.org/lesson/701337/step/7?auth=login&unit=701406
# Соберите данные со всех 5 категорий на сайте тренажере=http://parsinger.ru/html/index1_page_1.html
# и соберите все данные с карточек # + ссылка на карточку с товаром.
#
# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.
#
# Пример:
# [
#   {
#       "categories": "mobile",
#       "name": "",
#       "article": "",
#       "description": {
#           "brand": "",
#           "model": "",
#           "material": "",
#           "type_display": "",
#           "diagonal": "" ,
#           size: "",
#           "weight": "",
#           "resolution": "",
#           site: ""
#       },
#       "count": "",
#       "price": "",
#       "old_price": "",
#       "link": ""
#   },
#
# Вставьте код в поле ниже и отправьте его на рецензию.

# Решение мое
# 1 создаем функции:
# def get_soup(url: str) -> BeautifulSoup: - возвращает BeautifulSoup для url
# def all_cards_urls(url: str) -> list: - возвращает список ссылок для всех карточек товаров со всех станиц
# всех категорий сайта-тренажера
# def get_page_data(all_cards_urls: list) ->  list:- возвращает список result_json в который собраны необходимые данные
# всех карточек товаров со всех станиц всех категорий сайта-тренажера
# def save_to_file(result_json: list, filename: str) -> None: - записывает result_json в итоговый файл filename
# # 2 Основное тело программы if __name__ == '__main__':
# 1. Формируем список ссылок для всех карточек товаров со всех станиц всех категорий сайта-тренажера
# def all_cards_urls(url: str) -> list:
# 2. Создаем  список result_json в который собираются необходимые данные всех карточек товаров со всех станиц
# всех категорий сайта-тренажера
# def get_page_data(all_cards_urls: list) ->  list:
# 3. Записываем  result_json в итоговый файл res4.json
# def save_to_file(result_json: list, filename: str) -> None:


# импортируем нужные библиотеки
from bs4 import BeautifulSoup
import requests
import json


# 1 создаем функции:
# def get_soup(url: str) -> BeautifulSoup: - возвращает BeautifulSoup для url
def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# def all_cards_urls(url: str) -> list: - возвращает список ссылок для всех карточек товаров со всех станиц
# всех категорий сайта-тренажера
def all_cards_urls(url: str) -> list:
    global cat_names
    soup = get_soup(url)
    schema = 'https://parsinger.ru/html/'
    cat_names = [cat.div['id'] for cat in soup.find('div', class_='nav_menu').find_all('a')]
    page_links = []
    for cat_n, cat_name in enumerate(cat_names):
        for page_n in range(1, 33):
            page_links.append(f"{schema}{cat_name}/{cat_n + 1}/{cat_n + 1}_{page_n}.html")
    return page_links


# def get_page_data(all_cards_urls: list) ->  list:- возвращает список result_json в который собраны необходимые данные
# всех карточек товаров со всех станиц всех категорий сайта-тренажера
def get_page_data(page_links: list) -> list:
    result_json = []
    for url in page_links:
        soup = get_soup(url)
        # на адресе карточки собираем необходимые данные
        name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
        article = [x.text.strip('Артикул:  ') for x in soup.find_all('p', class_='article')]
        # ключи для словаря description
        ids = [li['id'] for li in soup.select('li[id]')]
        # значения ля словаря description
        val = soup.find('ul', id='description').find_all('li')
        # словарь description
        description = {}
        for n in range(len(ids)):
            description[ids[n]] = val[n].text[val[n].text.find(':') + 1:].strip()
        count = [x.text.strip()[x.text.find(':') + 2:] for x in soup.find_all('span', id='in_stock')]
        price = [x.text for x in soup.find('div', class_='sale').find_all('span', id='price')]
        old_price = [x.text for x in soup.find('div', class_='sale').find_all('span', id='old_price')]
        # складываем собранные данные в список result_json
        for name, article, count, price, old_price in zip(name, article, count, price,
                                                          old_price):
            result_json.append({
                'categories': url[26:-11].strip('/'),
                'name': name,
                'article': article,
                'description': description,
                'count': count,
                'price': price,
                'old_price': old_price,
                'link': url
            })
    return result_json


# def save_to_file(result_json: list, filename: str) -> None: - записывает result_json в итоговый файл filename
def save_to_file(result_json: list, filename: str) -> None:
    """Save json data to file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)


# 2 Основное тело программы
if __name__ == '__main__':
    # Формируем список ссылок для всех карточек товаров со всех станиц всех категорий сайта-тренажера
    page_links = all_cards_urls('http://parsinger.ru/html/index1_page_1.html')
    # Собираем в список result_json необходимые данные карточек товаров со всех станиц всех категорий сайта-тренажера
    result_json = get_page_data(page_links)
    # Записываем  result_json в итоговый файл parsing_4_10
    save_to_file(result_json, 'parsing_4_10.json')

# https://stepik.org/review/reviews/3370071?auth=login&unit=701406
# Условие:
# Выберите 1 любую категорию на сайте тренажёре=http://parsinger.ru/html/index3_page_1.html,
# и соберите все данные с карточек товаров + ссылка на карточку.
#
# По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела.
# Ключи в блоке description должны быть получены автоматически из атрибутов HTML элементов.
#
# Пример:
# [
#   {
#       "categories": "watch",
#       "name": "Jet Kid Start blue Умные детские часы",
#       "article": "80235265",
#       "description": {
#           "brand": "Jet",
#           "model": "Excidium",
#           "type": "умные часы",
#           "display": "Монохромный",
#           "material_frame": "пластик" ,
#           "material_bracer": "силикон",
#           size: "54х34х12 мм",
#           site: "www.jetdevice.com"
#       },
#       "count": "",
#       "price": "",
#       "old_price": "",
#       "link": ""
#   },

# Вставьте код в поле ниже и отправьте его на рецензию.


# Решение # 948400270
import json
import logging

import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s, %(asctime)s'
)


def get_soup(url: str) -> BeautifulSoup:
    """Make BeautifulSoup object from link."""
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


def get_pages(url: str) -> list:
    """Generate links."""
    soup = get_soup(url)
    schema = 'https://parsinger.ru/html/'
    pages = [f"{schema}{link['href']}"
             for link in soup.find('div', class_='pagen').find_all('a')]
    links = []
    with tqdm(total=len(pages)) as pbar:
        for page in pages:
            pbar.set_description('Generating category items links')
            links.extend([f"{schema}{link['href']}" for link in
                          get_soup(page).find_all('a', class_='name_item')])
            pbar.update()
    logging.info('All items links generated')
    return links


def get_categories(url: str) -> tuple:
    """Generate lists with categories names and links."""
    soup = get_soup(url)
    schema = 'https://parsinger.ru/html/'
    cat_urls = [f"{schema}{link['href']}" for link in
                soup.find('div', class_='nav_menu').find_all('a')]
    names_list = [name.text for name in
                  soup.find('div', class_='nav_menu').find_all('a')]
    cat_names = [cat.div['id'] for cat in
                 soup.find('div', class_='nav_menu').find_all('a')]
    return cat_urls, names_list, cat_names


def get_page_data(soup: BeautifulSoup) -> tuple:
    """Parsing required data from soup object."""
    name = soup.find('p', id='p_header').text.strip()
    article = soup.find('p', class_='article').text.split(': ')[1].strip()
    price = soup.find('span', id='price').text.strip()
    old_price = soup.find('span', id='old_price').text.strip()
    count = soup.find('span', id='in_stock').text.split(': ')[1].strip()
    description = {item.attrs['id']: item.text.split(': ')[1] for item in
                   soup.find_all('li')}
    return name, article, price, old_price, count, description


def save_to_file(result_json: list, filename: str) -> None:
    """Save json data to file."""
    logging.info(f'Saving data to {filename}...')
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
    logging.info(f'{filename} is ready!')


if __name__ == '__main__':
    # Getting category data
    logging.info('Getting category data...')
    cat_urls, names_list, cat_names = get_categories(
        'https://parsinger.ru/html/index1_page_1.html')

    # Choose category to parse
    print('\n'.join([f"{i + 1}:{name}" for i, name in enumerate(names_list)]))
    x = int(input('Enter number category to parse: '))
    cat_url, cat_name, cat_header = cat_urls[x - 1], names_list[x - 1], cat_names[x - 1]

    # Generate links
    urls_list = get_pages(cat_url)

    # Parse data
    result_json = []
    with tqdm(total=len(urls_list)) as pbar:
        pbar.set_description(f'Parsing data from category "{cat_name}"')
        for url in urls_list:
            name, article, price, old_price, count, description = get_page_data(get_soup(url))
            result_json.append({
                'categories': cat_header,
                'name': name,
                'article': article,
                'description': description,
                'count': count,
                'price': price,
                'old_price': old_price,
                'link': url
            })
            pbar.update()

    # Save data to file
    save_to_file(result_json, 'parsing_4_10.json')

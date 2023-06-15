# https://stepik.org/lesson/715954/step/13?unit=716748

# Задача
# Откройте сайт=http://parsinger.ru/infiniti_scroll_3/ с помощью Selenium
# На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100 элементов;
# Необходимо прокрутить все окна в самый низ;
# Цель: получить все значение в каждом из окошек и сложить их;
# Получившийся результат вставить в поле ответа.

# Павел Хошев в прошлом году

# Степан Лукашевич 8 месяцев назад
# Так и не разобрался с ActionChains - не потребовались просто. Окна отлично скролятся через:
#
# browser.execute_script("return arguments[0].scrollIntoView(true);", item)
#  Как и прошлые - решил через рекурсию. Чувствую, что мог бы аккуратнее и красивее, но как есть) 9 секунд на все,
#  вместе с 0.5 сном

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def recurs_search(items, input_items, browser, container, sum_num):
    if not items:
        return sum_num

    for index, item in enumerate(items):
        browser.execute_script("return arguments[0].scrollIntoView(true);", item)
        sum_num += int(item.text)
        input_items.append(item)

    new_items = [x for x in container.find_elements(By.TAG_NAME, 'span') if x not in input_items]

    return recurs_search(new_items, input_items, browser, container, sum_num)


def main():
    st = time.time()
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_3/')
        time.sleep(0.5)
        scroll_containers = [x for x in browser.find_element(By.CLASS_NAME, 'main').find_elements(By.TAG_NAME, 'div')
                             if 'scroll-container' in x.get_attribute('id')]
        all_sum = 0
        for container in scroll_containers:
            input_list = []
            start_items = container.find_elements(By.TAG_NAME, 'span')
            all_sum += recurs_search(start_items, input_list, browser, container, 0)

        print(all_sum)
        print(f'Время выполнения: {round(time.time() - st, 2)} секунд')


if __name__ == '__main__':
    main()
# >>>159858750

# https://stepik.org/lesson/715954/step/5?unit=716748

# Прокрутка содержимого страницы - способ 2 Keys()
# Для понимания следующего примера откройте любой степ на степике, у которого более 100 комментариев, и попробуйте
# пролистать к самому последнему комментарию. Вы увидите несколько загрузок с сервера. Приведенный выше пример с циклом
# for обработал бы только первые 17 элементов, т.к. они были бы загружены при открытии страницы. Чтобы решить эту
# проблему и обрабатывать все подгружаемые элементы, давайте модифицируем этот код.
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')

    list_input = []
    # Мы добавили бесконечный цикл while для того, чтобы добраться абсолютно до всех элементов на странице, в этом коде
    # отсутствует условие прерывание бесконечного цикла, но об этом поговорим дальше.
    while True:
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]  # генерирует список из всех найденных на
        # странице элементов, тегов <input>, при каждой новой загрузке данных с сервера.
        for tag_input in input_tags:
            if tag_input not in list_input:  # это условие проверяет, есть ли элемент в контрольном списке list_input.
                # Если элемент отсутствует, то совершаем взаимодействие tag_input.click()
                tag_input.send_keys(Keys.TAB)  # .DOWN
                # tag_input.click()
                time.sleep(1)
                list_input.append(tag_input)  # в конце цикла for,  добавляет элемент в список list_input, который мы
                # создали для того, чтобы хранить все элементы, с которыми уже взаимодействовали, чтобы не
                # взаимодействовать с ним дважды.

# Мы совсем чуть-чуть усложнили этот код =).
# Запустите последний пример у себя в терминале и понаблюдайте за происходящим всё куда проще, чем кажется.
# Доступные к применению клавиши
# ADD	ALT	ARROW_DOWN
# ARROW_LEFT	ARROW_RIGHT	ARROW_UP
# BACKSPACE	BACK_SPACE	CANCEL
# CLEAR	COMMAND	CONTROL
# DECIMAL	DELETE	DIVIDE
# DOWN	UP	ENTER
# EQUALS	ESCAPE	F1
# F10	F11	F12
# F2	F3	F4
# F5	F6	F7
# F8	F9	HELP
# HOME	INSERT	LEFT
# LEFT_ALT	LEFT_CONTROL	LEFT_SHIFT
# META	MULTIPLY	NULL
# NUMPAD0	NUMPAD1	NUMPAD2
# NUMPAD3	NUMPAD4	NUMPAD5
# NUMPAD6	NUMPAD7	NUMPAD8
# NUMPAD9	PAGE_DOWN	PAGE_UP
# PAUSE	RETURN	RIGHT
# SEMICOLON	SEPARATOR	SHIFT
# SPACE	SUBTRACT
# TAB
#
# END

'''
Переход на Merion Academy

Напишите скрипт, который выполняет следующие шаги:

1. Открыть браузер chrome

2. Перейти на страницу google.com

3. В строке поиска написать Merion Academy

4. Нажать Enter (Keys.RETURN)

5. На странице с результатами выбрать первую ссылку и кликнуть на нее

6. После перехода, получить текущий URL:

 - Если URL начинается со строки https://wiki.merionet.ru, написать Добро пожаловать в Merion Academy!.

 - Иначе написать в консоль Мы попали куда-то не туда...



Рекомендуем выставить настройку implicitly_wait. Что это и зачем – разберем на уроке по ожиданиям.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.timeouts.implicit_wait = 10
browser.get('https://www.google.com/')
browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys('Merion Academy', Keys.RETURN)
browser.find_element(By.CSS_SELECTOR,
                     '.yuRUbf [jsname="UWckNb"][href="https://www.youtube.com/@merionacademy"]').click()

current_url = browser.current_url
if current_url.startswith('https://wiki.merionet.ru'):
    print('Добро пожаловать в Merion Academy!.')
else:
    print('Мы попали куда-то не туда... ')
browser.quit()

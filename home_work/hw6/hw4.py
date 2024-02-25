'''
Модальное окно

Напишите скрипт. Шаги:

1. Открыть страницу[http://the-internet.herokuapp.com/entry_ad](http://the-internet.herokuapp.com/entry_ad) ;

2. В модальном окне нажать на кнопку Сlose

3. Выведите в консоль текст элемента с id = content

>Подсказка: тут вам может понадобиться time.sleep(3)
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://the-internet.herokuapp.com/entry_ad')
time.sleep(3)
browser.find_element(By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p').click()

search_text = browser.find_element(By.CSS_SELECTOR, '#content').text
print(search_text)

browser.quit()
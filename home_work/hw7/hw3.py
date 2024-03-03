'''
Дождаться картинки

Напишите скрипт. Шаги:

1. Перейти на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html

2. Дождаться загрузки всех картинок

3. Получить значение атрибута src у 3й картинки

4. Вывести значение в консоль
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
browser.implicitly_wait(10)

award = browser.find_element(By.CSS_SELECTOR, '#award').get_dom_attribute('src')
print(award)

browser.quit()

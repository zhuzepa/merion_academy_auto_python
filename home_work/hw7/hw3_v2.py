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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
waiter = WebDriverWait(browser, 10, 1)

waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#award')))
award = browser.find_element(By.CSS_SELECTOR, '#award').get_dom_attribute('src')
print(award)

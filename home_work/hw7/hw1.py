"""
Нажатие на кнопку

Напишите скрипт. Шаги:

1. Перейти на страницу http://uitestingplayground.com/ajax

2. Нажать на синюю кнопку

3. Получить текст из зеленой плашки

4. Вывести его в консоль (”Data loaded with AJAX get request.”)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://uitestingplayground.com/ajax')

browser.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
browser.implicitly_wait(20)

text_ajax = browser.find_element(By.CSS_SELECTOR, '.bg-success').text
print(text_ajax)
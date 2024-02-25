'''
Поле ввода

Напишите скрипт. Шаги:

1. http://the-internet.herokuapp.com/inputs

2. Введите в поле текст 1000

3. Очистите это поле (метод `clear`)

4. введите в это же поле текст 2000
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://the-internet.herokuapp.com/inputs')

input_br = browser.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_br.send_keys('1000')
input_br.clear()
input_br.send_keys('2000')

browser.quit()

'''
Переименовать кнопку

Напишите скрипт. Шаги:

1. Перейти на сайт http://uitestingplayground.com/textinput

2. Указать в поле ввода текст "Merion"

3. Нажать на синюю кнопку

4. Получить текст кнопки и вывести в консоль (Merion)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://uitestingplayground.com/textinput')

browser.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys('Merion')
btn_text = browser.find_element(By.CSS_SELECTOR, '#updatingButton')
btn_text.click()

print(btn_text.text)
browser.quit()
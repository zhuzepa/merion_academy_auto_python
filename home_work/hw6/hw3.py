'''
Клик по кнопке с css-классом

Напишите скрипт. Шаги:

1. Открыть страницу http://uitestingplayground.com/classattr

2. Кликнуть на синюю(!) кнопку

3. Запустите скрипт 3 раза. Убедитесь, что код не требуется редактировать – скрипт всегда работает.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://uitestingplayground.com/classattr')

browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()

browser.quit()
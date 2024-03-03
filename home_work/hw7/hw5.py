'''
Скрипт на калькулятор

Напишите скрипт. Шаги:

1. Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html

2. В поле ввода по локатору #delay ввести значение 45

3. Нажать на кнопки

    1. 7

    2. + (плюс)

    3. 8

    4. =

4. Дождаться результата. Вывести его в консоль.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
waiter = WebDriverWait(browser, 10, 1)

delay_btn = browser.find_element(By.CSS_SELECTOR, '#delay')
delay_btn.clear()
delay_btn.send_keys('4')

browser.find_element(By.CSS_SELECTOR, '.keys span:nth-child(1)').click()
browser.find_element(By.CSS_SELECTOR, '.keys span:nth-child(4)').click()
browser.find_element(By.CSS_SELECTOR, '.keys span:nth-child(2)').click()
browser.find_element(By.CSS_SELECTOR, '.keys span:nth-child(15)').click()

waiter.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#spinner')))


result = browser.find_element(By.CSS_SELECTOR, '.screen').text

print(result)
browser.quit()

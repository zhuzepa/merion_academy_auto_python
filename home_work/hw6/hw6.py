'''Форма авторизации

Напишите скрипт, шаги:

1. Открыть страницу [http://the-internet.herokuapp.com/login](http://the-internet.herokuapp.com/login)

2. В поле uername ввести значение *`tomsmith`*

3. В поле password ввести значение *`SuperSecretPassword!`*

4. Нажмите кнопку Login

5. Выведите в консоль текст появившейся зеленой плашки'''

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/login')
browser.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
browser.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
browser.find_element(By.CSS_SELECTOR, '.radius').click()

text_login = browser.find_element(By.CSS_SELECTOR, '#flash').text
print(text_login)

browser.quit()
'''
Напишите скрипт для работы с интернет-магазином. Шаги

1. Открыть сайт магазина https://www.saucedemo.com/

2. Авторизоваться под пользователем standard_user

3. Добавить в корзину товары:

    1. Sauce Labs Backpack

    2. Sauce Labs Bolt T-Shirt

    3. Sauce Labs Onesie

4. Перейти в корзину

5. Нажать Checkout

6. Заполнить форму данными:

    1. Имя

    2. Фамиля

    3. Почтовый индекс

7. Нажать continue

7. Прочитать со стрницы итоговую стоимость ( Total )

8. Закрыть браузер

9. Вывести в консоль итоговую стоимость
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

faker = Faker()
faker_jp = Faker('ja_JP')
browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com/')
browser.implicitly_wait(10)

browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
browser.find_element(By.CSS_SELECTOR, '#login-button').click()

items_to_add = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
items = browser.find_elements(By.CSS_SELECTOR, '.inventory_item')

for item in items:
    if item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text in items_to_add:
        item.find_element(By.CSS_SELECTOR, 'button').click()

browser.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
browser.find_element(By.CSS_SELECTOR, '#checkout').click()

browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys(faker_jp.first_name())
browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys(faker_jp.last_name())
browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('12345678')

browser.find_element(By.CSS_SELECTOR, '#continue').click()
total = browser.find_element(By.CSS_SELECTOR, '.summary_total_label').text

browser.quit()
print(total)




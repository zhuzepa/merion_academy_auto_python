'''
Скрипт заполнения формы

Напишите скрипт. Шаги:

1. Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html

2. Заполнить форму значениями

Поле	Значение
First name	Иван
Last name	Петров
Address	Ленина, 55-3
Zip code	*оставить пустым
City	Москва
Country	Россия
E-mail	*оставить пустым
Phone number	*оставить пустым
Job position	QA
Company	Merion
3. Нажать кнопку Submit

4. Вывести в консоль цвет полей Zip code, E-mail и Phone (background-color)
'''

from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

fake = Faker()
fake_ru = Faker('ru_RU')

browser.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys(fake_ru.first_name())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="last-name"]').send_keys(fake_ru.last_name())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(fake_ru.address())

browser.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys(fake_ru.city())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys(fake_ru.country())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys(fake_ru.email())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys(fake_ru.phone_number())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys(fake_ru.job())
browser.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys(fake_ru.company())

browser.find_element(By.CSS_SELECTOR, '.btn').click()

color_zip = browser.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')

print(color_zip)

browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/login')

button = browser.find_element(By.CSS_SELECTOR, '.radius')

value_l = button.value_of_css_property('line-height')
value_f = button.value_of_css_property('font-family')
value_b = button.value_of_css_property('border-style')
value_c = button.value_of_css_property('cursor')

if value_l == 'solid':
    print('Твердый')
else:
    print('Мягкий')

if 'Helvetica' in value_f:
    print('Helvetica')
else:
    print('Другой')


browser.quit()
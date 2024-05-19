from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# открывается и настраивается драйвер
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.labirint.ru/')
driver.implicitly_wait(5)

# вход на главную страницу
driver.find_element(By.CSS_SELECTOR, 'button.cookie-policy__button').click()

# поиск на главное странице
driver.find_element(By.CSS_SELECTOR, 'span #search-field').send_keys('Python', Keys.RETURN)

# выбор книги на странице с результатами
driver.find_element(By.CSS_SELECTOR, '.product-card__name').click()

# добавление книги в корзину со страницы товара
driver.find_element(By.CSS_SELECTOR, '.btn-buy').click()

# проверка счетчика корзины
counter = driver.find_element(By.CSS_SELECTOR, '.basket-in-cart-a').text

print(counter == '1')


driver.quit()
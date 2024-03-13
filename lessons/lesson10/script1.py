from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.labirint.ru/')
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, 'button.cookie-policy__button').click()
driver.find_element(By.CSS_SELECTOR, 'span #search-field').send_keys('Python', Keys.RETURN)
driver.find_element(By.CSS_SELECTOR, '.product-card__name').click()


driver.quit()
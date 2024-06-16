from selenium import webdriver
from home_work.hw8.task4.purchase import Purchase

driver = webdriver.Chrome()

purch = Purchase(driver)
purch.open()
purch.auth('standard_user', 'secret_sauce')

purch.add_items()
purch.checkout()
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com/')
browser.implicitly_wait(10)

browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
browser.find_element(By.CSS_SELECTOR, '#login-button').click()


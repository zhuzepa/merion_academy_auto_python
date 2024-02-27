from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/login')

browser.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
browser.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
browser.find_element(By.CSS_SELECTOR, '.radius').click()

txt = browser.find_element(By.CSS_SELECTOR, '#flash').text

print(txt[:-1])

browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/dynamic_controls')

remove_button = browser.find_element(By.CSS_SELECTOR, '#checkbox-example button')
print(remove_button.is_displayed())

text_input = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
print(text_input.is_enabled())

checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
print(checkbox.is_selected())
checkbox.click()
print(checkbox.is_selected())

browser.quit()
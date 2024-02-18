from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/")
browser.find_element(By.CSS_SELECTOR, 'li > a[href="/dynamic_controls"]').click()

browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
browser.find_element(By.CSS_SELECTOR, "#checkbox-example  button").click()
browser.find_element(By.CSS_SELECTOR, "#checkbox-example  button").click()

browser.quit()
a = 1

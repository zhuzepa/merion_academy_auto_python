from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://the-internet.herokuapp.com/inputs")
element = browser.find_element(By.CSS_SELECTOR, "[type=number]")
element.send_keys("1234")

browser.quit()

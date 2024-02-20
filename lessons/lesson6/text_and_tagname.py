from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/")

links = browser.find_elements(By.CSS_SELECTOR, "#content li")

for link in links:
    print(link.tag_name, link.text)

browser.quit()

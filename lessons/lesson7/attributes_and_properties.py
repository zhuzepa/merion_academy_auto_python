from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://ya.ru/")

element = browser.find_element(By.CSS_SELECTOR, "#text")

print(element.get_dom_attribute("autocorrect"))
print(element.get_property("ariaAutoComplete"))
browser.quit()

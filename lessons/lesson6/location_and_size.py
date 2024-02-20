from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/login")

username_input = browser.find_element(By.CSS_SELECTOR, "#username")
password_input = browser.find_element(By.CSS_SELECTOR, "#password")

username_input_y = username_input.location.get("y")
password_input_y = password_input.location.get("y")

if username_input_y > password_input_y:
    print("Username выше")
else:
    print("Pass выше")

if username_input.size.get("width") == password_input.size.get("width"):
    print("Элементы равны")
else:
    print("Не равны")

browser.quit()

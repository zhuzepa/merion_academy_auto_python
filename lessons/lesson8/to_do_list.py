# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://sky-todo-list.herokuapp.com/')
# sleep(5)
# todo_lists = browser.find_elements(By.CSS_SELECTOR, 'td')
# for todo_list in todo_lists:
#     print(todo_list.text)
#
# browser.quit()

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://sky-todo-list.herokuapp.com/")

element = WebDriverWait(browser, 10).until(EC.text())

todo_lists = browser.find_elements(By.CSS_SELECTOR, "td")
for todo_list in todo_lists:
    print(todo_list.text)

browser.quit()

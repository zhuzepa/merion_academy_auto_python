'''
Напишите скрипт. Шаги:

1. Открыть страницу http://the-internet.herokuapp.com/add_remove_elements/

2. 5 раз кликнуть на кнопку Add Element

3. Собрать со страницы список кнопок Delete

4. Вывести на экран размер списка
'''

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# b = webdriver.Chrome()
# b.get('http://the-internet.herokuapp.com/add_remove_elements/')
# element_click = b.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
# list_delete = []
# for _ in range(5):
#     element_click.click()
#     b.find_element(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
#     list_delete.append(1)
#
# print(list_delete)
# b.quit()


# version 2

from selenium import webdriver
from selenium.webdriver.common.by import By

browser  = webdriver.Chrome()
browser.get('http://the-internet.herokuapp.com/add_remove_elements/')
bk = browser.find_element(By.CSS_SELECTOR, '.example button')
bk.click()
bk.click()
bk.click()
bk.click()
bk.click()

delete_button = browser.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print(len(delete_button))

delete_button_2 = browser.find_element(By.CSS_SELECTOR, '#elements').find_elements(By.CSS_SELECTOR, 'button')
print(len(delete_button_2))

browser.quit()
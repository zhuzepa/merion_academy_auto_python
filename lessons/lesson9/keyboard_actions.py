from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

ActionChains(driver)\
    .key_down(Keys.CONTROL) \
    .send_keys('a')\
    .send_keys('c')\
    .key_up(Keys.CONTROL)\
    .perform()


'''
.key_down() зажимает кнопки и не отпускает
.key_up() отпускает кнопку
'''

driver.quit()

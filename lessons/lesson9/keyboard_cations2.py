from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

ActionChains(driver)\
    .send_keys_to_element(input, "Selenium python ")\
    .key_down(Keys.LEFT_SHIFT)\
    .send_keys(Keys.ARROW_UP)\
    .key_up(Keys.LEFT_SHIFT)\
    .key_down(Keys.CONTROL)\
    .send_keys("xvv", end=' ')\
    .key_up(Keys.CONTROL)\
    .key_down(Keys.CONTROL)\
    .send_keys_to_element(input, "vvv")\
    .key_up(Keys.CONTROL)\
    .perform()


driver.quit()

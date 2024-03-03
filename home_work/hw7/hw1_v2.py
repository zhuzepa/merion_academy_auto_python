from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get('http://uitestingplayground.com/ajax')
waiter = WebDriverWait(browser, 20, 1)

text_ajax = 'Data loaded with AJAX get request.'
browser.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.bg-success'), text_ajax))

print(text_ajax)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/progressbar")
waiter = WebDriverWait(browser, 60, 0.1)

text_to_be = "75"
browser.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter.until(
    EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, "#progressBar"), "aria-valuenow", text_to_be
    )
)

browser.find_element(By.CSS_SELECTOR, "#stopButton").click()

browser.quit()

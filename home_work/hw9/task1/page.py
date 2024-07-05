from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get('http://uitestingplayground.com/textinput')

    def send_text_button(self, value_button: str):
        self.driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys(value_button)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

    def text_button(self):
     return self.driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

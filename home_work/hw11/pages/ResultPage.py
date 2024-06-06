from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

    def text_button(self):
        text_btn = self.driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
        print(text_btn)

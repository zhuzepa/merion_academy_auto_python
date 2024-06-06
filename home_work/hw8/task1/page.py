from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("http://uitestingplayground.com/textinput")

    def search(self, term: str):
        self.driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys(term)

    def get_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

    def text_button(self):
        text_btn = self.driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
        print(text_btn)

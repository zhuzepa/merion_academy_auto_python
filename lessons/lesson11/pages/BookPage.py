from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lessons.lesson11.pages.BasePage import BasePage
from lessons.lesson11.pages.Header import Header


class BookPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-buy").click()
        # wait until cart rerender

    def is_plusone_enabled(self):
        button = self.driver.find_element(By.CSS_SELECTOR, ".plusone")
        is_displayed = button.is_displayed()
        is_enabled = button.is_enabled()
        return is_displayed and is_enabled
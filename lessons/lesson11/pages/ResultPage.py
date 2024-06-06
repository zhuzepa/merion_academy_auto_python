from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lessons.lesson11.pages.BasePage import BasePage


class ResultPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_book_page(self, index: int):
        self.driver.find_elements(By.CSS_SELECTOR, ".product-card__name")[index].click()

    def add_to_cart(self, index: int):
        self.driver.find_elements(By.CSS_SELECTOR, ".product-card .buy-link")[index].click()

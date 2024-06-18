from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self):
        self.driver.get('https://www.saucedemo.com/cart.html')

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()


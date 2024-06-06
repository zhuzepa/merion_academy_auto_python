from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Header:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_cart_counter(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.basket-in-cart-a.j-cart-count').text

    def get_logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.b-header-b-logo-e-logo-wrap')

    def search(self, term: str):
        self.driver\
            .find_element(By.CSS_SELECTOR, '#search-field')\
            .send_keys(term, Keys.RETURN)
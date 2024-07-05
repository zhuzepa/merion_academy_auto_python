from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutComplete:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get_status(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.header_secondary_container').text


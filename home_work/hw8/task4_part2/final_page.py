from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FinalPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def total_price(self):
        total = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return total
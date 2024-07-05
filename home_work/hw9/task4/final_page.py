from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from home_work.hw9.task4.checkout_coplete import CheckoutComplete


class FinalPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def total_price(self):
        total = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return total

    def items(self) -> list:
        return self.driver.find_elements(By.CSS_SELECTOR, '.cart_item')

    def finish(self):
        self.driver.find_element(By.CSS_SELECTOR, '#finish').click()
        return CheckoutComplete(self.driver)



from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ContactPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def user_date(self, first_name: str, last_name: str, zipp: int):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(zipp)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

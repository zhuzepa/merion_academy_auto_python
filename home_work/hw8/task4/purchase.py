from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Purchase:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self):
        self.driver.get('https://www.saucedemo.com/')

    def auth(self, name, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_items(self):
        items_to_add = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie',
                        'Test.allTheThings() T-Shirt (Red)']
        items = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item')

        for item in items:
            if item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text in items_to_add:
                item.find_element(By.CSS_SELECTOR, '.btn_primary ').click()

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def user_date(self, first_name: str, last_name: str, zipp: int):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(zipp)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def total_price(self):
        total = self.driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        return total

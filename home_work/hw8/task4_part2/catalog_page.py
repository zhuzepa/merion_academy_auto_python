from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CatalogPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # def add_item_to_cart(self, item_name):
    #     items = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item')
    #
    #     for item in items:
    #         if item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text == item_name:
    #             item.find_element(By.CSS_SELECTOR, '.btn_primary ').click()

    def add_items_to_cart(self, item_list_name):
        items = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item')

        for item in items:
            if item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text in item_list_name:
                item.find_element(By.CSS_SELECTOR, '.btn_primary ').click()

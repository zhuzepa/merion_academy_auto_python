from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Form:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def set_value_for(self, field_name, field_value):
        self.driver.find_element(By.CSS_SELECTOR, f'.form-control[name={field_name}]').send_keys(field_value)

    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '.btn-outline-primary').click()

    def get_background_color(self, selector, property_name):
       return self.driver.find_element(By.CSS_SELECTOR, selector).value_of_css_property(property_name)
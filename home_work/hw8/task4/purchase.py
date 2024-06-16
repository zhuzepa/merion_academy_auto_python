from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Purchase:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self):
       self.driver.get('https://www.saucedemo.com/')

    def auth(self, name, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
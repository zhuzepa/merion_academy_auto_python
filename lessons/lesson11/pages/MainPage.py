from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lessons.lesson11.pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://www.labirint.ru")
        self.driver.add_cookie({'name': 'cookie_policy', 'value': '1'})
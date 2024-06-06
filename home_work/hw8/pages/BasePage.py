from selenium.webdriver.remote.webdriver import WebDriver

from lessons.lesson11.pages.Header import Header


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.header = Header(driver)

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class DriverManager:
    def __init__(self) -> None:
        pass

    def get(self, browser_name="chrome") -> WebDriver:
        if browser_name.startswith("ch"):
            self.driver = webdriver.Chrome()
        elif browser_name.startswith("f"):
            self.driver = webdriver.Firefox()
        elif browser_name.startswith("saf"):
            self.driver = webdriver.Safari()
        else:
            print("Unkown driver name")

        self.configure()
        return self.driver

    def quit(self):
        if self.driver != None:
            self.driver.quit()

    def configure(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

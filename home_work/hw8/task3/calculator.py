from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.delay_time = 1

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, time_delay):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time_delay)
        self.delay_time = time_delay

    def press(self, number):
        self.driver.find_element(
            By.CSS_SELECTOR, f".keys span:nth-child({number})"
        ).click()

    def get_result(self):
        waiter = WebDriverWait(self.driver, self.delay_time, 0.1)
        waiter.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#spinner")))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

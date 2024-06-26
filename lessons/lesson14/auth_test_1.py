from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

test_data = [
    ("tomsmith", "WRONG_PASS", "Your password is invalid!"),
    ("WRONG_USERNAME", "SuperSecretPassword", "Your username is invalid!"),
]


@pytest.mark.parametrize(
    "username, password, error_text", test_data, ids=["Test_1", "Test_2"]
)
def test_password_invalid(username: str, password: str, error_text: str):
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.CSS_SELECTOR, "#username").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    log_invalid = driver.find_element(By.CSS_SELECTOR, "#flash").text
    driver.quit()

    assert log_invalid.startswith(error_text)

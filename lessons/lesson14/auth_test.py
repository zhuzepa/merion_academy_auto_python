from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_auth():
    """Тест, где проверяем успешную авторизацию.
    Должен отображаться текст You logged onto a secure area!"""

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)

    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    logged = driver.find_element(By.CSS_SELECTOR, "#flash").text
    logout = driver.find_element(By.CSS_SELECTOR, "a.button").text

    href = driver.find_element(By.CSS_SELECTOR, "a.button")
    attribute_href = href.get_attribute("href")
    driver.quit()

    assert attribute_href.endswith("/logout")
    assert logged.startswith("You logged into a secure area!")
    assert logout == "Logout"


def test_password_invalid():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    log_invalid = driver.find_element(By.CSS_SELECTOR, "#flash").text
    driver.quit()

    assert log_invalid.startswith("Your password is invalid!")


def test_login_invalid():
    driver = webdriver.Firefox()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    log_invalid = driver.find_element(By.CSS_SELECTOR, "#flash").text
    driver.quit()

    assert log_invalid.startswith("1Your username is invalid!")

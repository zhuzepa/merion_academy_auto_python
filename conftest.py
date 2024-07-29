import pytest
from selenium import webdriver
import requests

base_url = "https://x-clients-be.onrender.com"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


@pytest.fixture
def url():
    return "https://www.ebay.com/"


@pytest.fixture  # получаем токен и передаем его в тестах
def get_token():
    body_params = {"username": "leyla", "password": "water-fairy"}
    response = requests.post(base_url + "/auth/login", json=body_params)
    return response.json().get("userToken")

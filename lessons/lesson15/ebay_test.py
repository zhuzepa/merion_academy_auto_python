from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_ebay(browser, url: str):
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, ".carousel__snap-point").click()
    items = browser.find_elements(By.CSS_SELECTOR, ".carousel__snap-point")
    items[-1].click()
    browser.find_element(By.CSS_SELECTOR, "#atcBtn_btn_1").click()
    price_on_card = browser.find_element(By.CSS_SELECTOR, '.x-price-primary').text
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-testid="x-atc-action"]'),
        "Просмотреть в корзине")
    )
    car = browser.find_element(By.CSS_SELECTOR, ".gh-cart-icon")
    ActionChains(browser).move_to_element(car).perform()
    total = browser.find_element(By.CSS_SELECTOR, ".total-val").text
    assert total == price_on_card

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import MainPage

# открытие драйвера и настройка

driver = webdriver.Firefox()


def settings_open():
    driver.maximize_window()
    driver.implicitly_wait(4)





def go_card_page():
    driver.find_element(By.CSS_SELECTOR, ".product-card__name").click()


def click_on_buy_button():
    driver.find_element(By.CSS_SELECTOR, ".btn-buy").click()


def click_on_buy_button_on_result_page():
    driver.find_element(By.CSS_SELECTOR, '.product-card .buy-link').click()


def get_cart_count():
    return driver.find_element(By.CSS_SELECTOR, ".basket-in-cart-a").text


def plus_one_button():
    return driver.find_element(By.CSS_SELECTOR, '.plusone')


def close_driver():
    driver.quit()


def test_1():
    settings_open()
    open_main_page()
    search_site('python')
    go_card_page(0)
    click_on_buy_button()

    counter = get_cart_count()
    print(counter == '1')
    close_driver()


def test_2():
    settings_open()
    open_main_page()
    search_site('css')
    click_on_buy_button_on_result_page(0)
    go_card_page(0)

    plusone = get_cart_count()
    is_displayed = plusone.is_displayed()
    is_visible = plusone.is_enabled()

    # проверка счетика корзины
    counter = get_cart_count()
    print(counter == "1")
    print(is_displayed)
    print(is_visible)
    close_driver()


test_1()
test_2()

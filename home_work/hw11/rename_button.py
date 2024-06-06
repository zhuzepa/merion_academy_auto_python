from home_work.hw11.pages.MainPage import MainPage
from home_work.hw11.pages.ResultPage import ResultPage

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    main = MainPage(driver)
    main.open()
    main.search('I am is super AQA')

    result = ResultPage(driver)
    result.click_button()
    result.text_button()

    driver.quit()

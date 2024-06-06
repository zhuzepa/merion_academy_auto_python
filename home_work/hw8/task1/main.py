from home_work.hw8.task1.page import Page
from selenium import webdriver



def test_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)
    main = Page(driver)
    main.open()
    main.search('I am is super AQA')
    main.get_button()
    main.text_button()

    driver.quit()

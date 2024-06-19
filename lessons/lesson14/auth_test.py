from selenium import webdriver
from selenium.webdriver.common.by import By


def login_auth():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/login')

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

    logged = driver.find_element(By.CSS_SELECTOR, '#flash').text
    if 'You logged into a secure area!' in logged:
        print('Успешный вход')
    else:
        print("Текст входа не соответствует ожидаемому.")

    logout = driver.find_element(By.CSS_SELECTOR, 'a.button').text
    if 'Logout' in logout:
        print('Кнопка выхода присутствует')
    else:
        print('Что-то пошло не так')

    href = driver.find_element(By.CSS_SELECTOR, 'a.button')
    attribute_href = href.get_attribute('href')
    print(attribute_href)


login_auth()

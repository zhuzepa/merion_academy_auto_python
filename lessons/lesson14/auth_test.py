from selenium import webdriver
from selenium.webdriver.common.by import By


def login_auth():
    """Тест, где проверяем успешную авторизацию.
    Должен отображаться текст You logged onto a secure area!"""


    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)

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


def password_invalid():
    driver = webdriver.Firefox()
    driver.get('https://the-internet.herokuapp.com/login')

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

    log_invalid = driver.find_element(By.CSS_SELECTOR, '#flash').text
    if 'Your password is invalid!' in log_invalid:
        print('Проверьте пароль')
    else:
        print("Успешный вход")

    driver.quit()


password_invalid()


def login_invalid():
    driver = webdriver.Firefox()
    driver.get('https://the-internet.herokuapp.com/login')

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

    log_invalid = driver.find_element(By.CSS_SELECTOR, '#flash').text
    if 'Your username is invalid!' in log_invalid:
        print('Проверьте логин')
    else:
        print("Успешный вход")

    driver.quit()


login_invalid()

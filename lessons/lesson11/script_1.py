from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# открытие драйвера и настройка
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(4)

# вход на главную страницу
driver.get("https://www.labirint.ru/")
my_cookie = {"name": "cookie_policy", "value": "1"}
driver.add_cookie(my_cookie)

# поиск на главной странице
driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys("python", Keys.ENTER)

# выбор книги на странице с результатами
driver.find_element(By.CSS_SELECTOR, ".product-card__name").click()

# добавление книги в корзину со странице товара
driver.find_element(By.CSS_SELECTOR, ".btn-buy").click()

# проверка счетика корзины
counter = driver.find_element(By.CSS_SELECTOR, ".basket-in-cart-a").text
print(counter == "1")

driver.quit()

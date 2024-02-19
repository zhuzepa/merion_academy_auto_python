import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.2048.org/")

body = browser.find_element(By.CSS_SELECTOR, "body")
game_over = False
for _ in range(1, 1000):
    body.send_keys(Keys.ARROW_UP)
    body.send_keys(Keys.ARROW_DOWN)
    body.send_keys(Keys.ARROW_RIGHT)
    body.send_keys(Keys.ARROW_LEFT)
    if browser.find_elements(By.CSS_SELECTOR, ".game-message.game-over"):
        game_over = True
        break

print("Игра окончена: ", game_over)
browser.quit()

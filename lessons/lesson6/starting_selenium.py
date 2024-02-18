from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://digital.dpprod.pgk.ru/auth/login")
browser.set_window_size(600, 800)


# browser.set_window_rect()
browser.maximize_window()
browser.minimize_window()
browser.fullscreen_window()
browser.save_screenshot("test.png")
# browser.find_element(By.CSS_SELECTOR, value='a[href="/windows/new"]').click()

browser.quit()

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://pgk.ru/")
print(browser.page_source)

browser.quit()

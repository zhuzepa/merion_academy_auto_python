from selenium import webdriver

js = "document.querySelector('div#mailbox').remove()"
browser = webdriver.Chrome()

browser.get("https://mail.ru/")
browser.save_screenshot("before.png")

browser.execute_script(js)
browser.save_screenshot("after.png")

browser.quit()

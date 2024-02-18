from selenium import webdriver


js_localstorage = 'localStorage.bestScore = 1000000000'

browser = webdriver.Chrome()
browser.get('https://www.2048.org/')
browser.execute_script(js_localstorage)
browser.refresh()
browser.save_screenshot('2048.png')
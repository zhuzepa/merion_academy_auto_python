from home_work.hw8.task3.calculator import Calculator
from selenium import webdriver

driver = webdriver.Chrome()

calc = Calculator(driver)
calc.open()

calc.set_delay(5)
calc.press(1)
calc.press(4)
calc.press(2)
calc.press(15)

res = calc.get_result()
print(res)

driver.quit()

from home_work.hw8.task2.form import Form
from selenium import webdriver

driver = webdriver.Chrome()

form = Form(driver)
form.open()

form.set_value_for('first-name','Гомер')
form.set_value_for('last-name','Гомеров')
form.set_value_for('address','Дом 742 по Вечнозелёной аллее')
form.set_value_for('city','Спринфилд')
form.set_value_for('country','Америка')
form.set_value_for('job-position','Engineer')
form.set_value_for('company','Спрингфилдской АЭС')

form.click_button()

zipcod = form.get_background_color('#zip-code', 'background-color')
email = form.get_background_color('#e-mail', 'background-color')
phone = form.get_background_color('#phone', 'background-color')

print(zipcod, email, phone, sep='\n')
driver.quit()
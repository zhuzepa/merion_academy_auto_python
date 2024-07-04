from home_work.hw8.task2.form import Form
from selenium import webdriver

green_color = 'rgba(209, 231, 221, 1)'
red_color = 'rgba(248, 215, 218, 1)'


def test_from(browser):
    form = Form(browser)
    form.open()

    form.set_value_for('first-name', 'Гомер')
    form.set_value_for('last-name', 'Гомеров')
    form.set_value_for('address', 'Дом 742 по Вечнозелёной аллее')
    form.set_value_for('city', 'Спринфилд')
    form.set_value_for('country', 'Америка')
    form.set_value_for('job-position', 'Engineer')
    form.set_value_for('company', 'Спрингфилдской АЭС')

    form.click_button()

    assert form.get_background_color('#first-name', 'background-color') == green_color
    assert form.get_background_color('#address', 'background-color') == green_color
    assert form.get_background_color('#city', 'background-color') == green_color
    assert form.get_background_color('#country', 'background-color') == green_color
    assert form.get_background_color('#job-position', 'background-color') == green_color

    assert form.get_background_color('#zip-code', 'background-color') == red_color
    assert form.get_background_color('#e-mail', 'background-color') == red_color
    assert form.get_background_color('#phone', 'background-color') == red_color


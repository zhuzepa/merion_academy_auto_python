from selenium import webdriver
from home_work.hw8.task4_part2.auth_page import AuthPage
from home_work.hw8.task4_part2.catalog_page import CatalogPage
from home_work.hw8.task4_part2.cart_page import CartPage
from home_work.hw8.task4_part2.contact_page import ContactPage
from home_work.hw8.task4_part2.final_page import FinalPage

driver = webdriver.Chrome()
auth = AuthPage(driver)
auth.open()
auth.auth('standard_user', 'secret_sauce')

catalog = CatalogPage(driver)
catalog.add_items_to_cart(['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie',
                           'Test.allTheThings() T-Shirt (Red)'])

cart = CartPage(driver)
cart.open()
cart.checkout()

contact = ContactPage(driver)
contact.user_date('Gomer', 'Simson', 777777)

final = FinalPage(driver)
print(final.total_price())

driver.quit()

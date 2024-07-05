from selenium import webdriver
from home_work.hw9.task4.auth_page import AuthPage
from home_work.hw9.task4.catalog_page import CatalogPage
from home_work.hw9.task4.cart_page import CartPage
from home_work.hw9.task4.contact_page import ContactPage
from home_work.hw9.task4.final_page import FinalPage


def test_shop(browser):
    auth = AuthPage(browser)
    auth.open()
    auth.auth('standard_user', 'secret_sauce')

    catalog = CatalogPage(browser)
    catalog.add_items_to_cart(['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie'])

    cart = CartPage(browser)
    cart.open()
    cart.checkout()

    contact = ContactPage(browser)
    contact.user_date('Gomer', 'Simson', 777777)

    final = FinalPage(browser)
    items_list = final.items()
    assert final.total_price().endswith('$58.29')
    assert len(items_list) == 3

    status = final.finish().get_status()
    assert status == 'Checkout: Complete!'


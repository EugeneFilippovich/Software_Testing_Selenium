from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from task13_high.pages.main_page import MainPage
from task13_high.pages.item_page import ItemPage
from task13_high.pages.cart_page import CartPage


class Application:

    """
    :type driver: selenium.webdriver.Chrome
    """

    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {"browser": "ALL"}

    def __init__(self):
        self.driver = webdriver.Chrome(desired_capabilities=Application.d)
        self.main_page = MainPage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()
        return self

    def main_page_load(self):
        self.main_page.open()
        return self

    def item_select(self):
        self.main_page.select_item()
        return self

    def item_to_cart(self):
        self.item_page.add_item('small')
        self.item_page.wait_cart_update()

    def checkout_items(self):
        self.item_page.checkout()

    def clear_cart(self):
        self.cart_page.remove_items()



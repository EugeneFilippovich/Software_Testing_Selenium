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

    def main_page_load(self):
        self.main_page.open()



from selenium import webdriver
from task13_high.pages.main_page import MainPage
from task13_high.pages.item_page import ItemPage
from task13_high.pages.cart_page import CartPage
import time


class Task:

    """
    :type driver: selenium.webdriver.Chrome
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def main_page_load(self):
        self.main_page.load_main_page()


a = Task()
a.main_page_load()
a.main_page.select_item()
time.sleep(2)
a.item_page.add_item('small')
time.sleep(2)
a.main_page_load()
a.main_page.select_item()
time.sleep(2)
a.item_page.add_item('small')
time.sleep(2)
a.main_page_load()
a.main_page.select_item()
time.sleep(2)
a.item_page.add_item('small')
time.sleep(2)
a.item_page.checkout()
time.sleep(2)
a.cart_page.remove_items()
time.sleep(2)
a.quit()
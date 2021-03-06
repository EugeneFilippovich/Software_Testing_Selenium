import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class ItemPage:

    """
     :type driver: selenium.webdriver.Chrome
     """

    def __init__(self, driver):
        self.driver = driver
        self.value = 1
        self.wait = WebDriverWait(self.driver, 10)

    def add_item(self, size):
        product_box = self.driver.find_element_by_id('box-product')
        add_to_cart = product_box.find_element_by_css_selector('[name = add_cart_product]')
        try:
            size_selection = Select(product_box.find_element_by_name('options[Size]'))
            size_selection.select_by_visible_text(size)
        except Exception:
            pass
        add_to_cart.click()
        return self

    def wait_cart_update(self):
        cart = self.driver.find_element_by_id('cart')
        try:
            self.wait.until(lambda d: cart.find_element_by_xpath('//span[starts-with(text(), {})]'.format(str(self.value))))
            if self.value < 3:
                self.value += 1
            else:
                time.sleep(1)
        except ValueError:
            print('Item has not been added to the cart!')
        return self

    def checkout(self):
        self.driver.find_element_by_link_text('Checkout »').click()
        return self

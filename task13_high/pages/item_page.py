

from selenium.webdriver.support.ui import Select


class ItemPage:

    """
     :type driver: selenium.webdriver.Chrome
     """

    def __init__(self, driver):
        self.driver = driver

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

    def checkout(self):
        self.driver.find_element_by_link_text('Checkout »').click()
        return self

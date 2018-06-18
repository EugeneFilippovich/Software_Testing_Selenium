from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CartPage:

    """
    :type driver: selenium.webdriver.Chrome
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remove_items(self):
        table = self.driver.find_element_by_id('order_confirmation-wrapper')
        lines = table.find_elements_by_css_selector('tr:not(.header):not(.footer)')
        view_port = self.driver.find_element_by_id('checkout-cart-wrapper')
        for _ in range(len(lines) - 3):
            remove_buttons = view_port.find_elements_by_css_selector('[value = Remove]')
            for double_ in remove_buttons:
                self.wait.until(EC.visibility_of(view_port.find_element_by_name('cart_form')))
                rmw = self.wait.until(EC.visibility_of(double_))
                rmw.click()
                self.wait.until(EC.staleness_of(lines[0]))
                break
            continue
        self.wait.until(EC.staleness_of(self.driver.find_element_by_id('box-checkout-summary')))
        return self

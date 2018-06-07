import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_10(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    wait = WebDriverWait(driver, 10)

    def log_in():
        driver.get("http://localhost/litecart/")

    def wait_cart_update(element):
        cart_items_quantity = 1
        try:
            element = wait.until(lambda d: element.find_element_by_partial_link_text(str(cart_items_quantity)))
            cart_items_quantity += 1
            print(cart_items_quantity)
        except ValueError:
            print('Item has not been added to the cart!')

    log_in()

    most_popular = driver.find_element_by_id('box-most-popular')
    most_popular_items = most_popular.find_elements_by_class_name('link')
    most_popular_items[0].click()

    product_box = driver.find_element_by_id('box-product')
    add_to_cart = product_box.find_element_by_css_selector('[name = add_cart_product]')
    try:
        size_selection = Select(product_box.find_element_by_name('options[Size]'))
        size_selection.select_by_visible_text('Small')
    except Exception:
        pass

    add_to_cart.click()

    cart = driver.find_element_by_id('cart')
    wait_cart_update(cart)




import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_10(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    cart_items_quantity = 0

    def log_in():
        driver.get("http://localhost/litecart/")

    most_popular = driver.find_element_by_id('box-most-popular')
    most_popular_items = most_popular.find_elements_by_class_name('link')
    most_popular_items[0].click()

    product_box = driver.find_element_by_id('box-product')
    add_to_cart = product_box.find_element_by_css_selector('[name = add_cart_product]')
    add_to_cart.click()

    cart = driver.find_element_by_id('cart')
    quantity = cart.find_element_by_class_name('quantity')


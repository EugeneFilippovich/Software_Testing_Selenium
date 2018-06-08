import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# С глобалом, да. Как-то без ООП можно было сделать?
cart_items_quantity = 1

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
        global cart_items_quantity
        try:
            element = wait.until(lambda d: element.find_element_by_xpath('//span[starts-with(text(), {})]'.format(str(cart_items_quantity))))
            if cart_items_quantity < 3:
                cart_items_quantity += 1
        except ValueError:
            print('Item has not been added to the cart!')

    def add_item_to_cart():
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



    log_in()

    add_item_to_cart()

    log_in()

    add_item_to_cart()

    log_in()

    add_item_to_cart()

    # количество в корзине обновляется, но в самой корзине элемента нет, поэтому time.sleep
    time.sleep(2)
    driver.find_element_by_link_text('Checkout »').click()
    print(cart_items_quantity)



    table = driver.find_element_by_id('order_confirmation-wrapper')
    lines = table.find_elements_by_css_selector('tr:not(.header):not(.footer)')

    def remove_item():
        view_port = driver.find_element_by_id('checkout-cart-wrapper')
        for _ in range(3, len(lines)):
            remove_buttons = view_port.find_elements_by_css_selector('[value = Remove]')
            for double_ in remove_buttons:
                rmw = wait.until(EC.visibility_of(double_))
                rmw.click()
                wait.until(EC.staleness_of(lines[0]))
                break


    remove_item()

    time.sleep(3)
    # откуда берется 5 элементов, если
    # for line in lines:
    #     item_line = line.find_element_by_xpath('.//*[contains(@class, item)]')
    #     print(item_line.text)
        # remove_button = driver.find_element_by_name('remove_cart_item')
        # remove_button.click()
        # time.sleep(2)
        # cart_items_quantity -= 1








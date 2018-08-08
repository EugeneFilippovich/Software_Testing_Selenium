import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# С глобалом, да. Как-то без ООП можно было сделать?
cart_items_quantity = 1

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_13(driver):
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


    # если бегать с дебагером, то без проблем все удаляет, находит. Если тест запустить, то при наличии 3 РАЗНЫХ уточек - последнюю не удаляет почему-то.
    # Там при появлении послднего элемента происходит задержка. Но ошибки никакой нет.
    def remove_item():
        table = driver.find_element_by_id('order_confirmation-wrapper')
        lines = table.find_elements_by_css_selector('tr:not(.header):not(.footer)')
        view_port = driver.find_element_by_id('checkout-cart-wrapper')
        for _ in range(len(lines) - 3):
            remove_buttons = view_port.find_elements_by_css_selector('[value = Remove]')
            for double_ in remove_buttons:
                wait.until(EC.visibility_of(view_port.find_element_by_name('cart_form')))
                rmw = wait.until(EC.visibility_of(double_))
                rmw.click()
                wait.until(EC.staleness_of(lines[0]))
                break
        wait.until(EC.staleness_of(driver.find_element_by_id('box-checkout-summary')))

    log_in()

    add_item_to_cart()

    log_in()

    add_item_to_cart()

    log_in()

    add_item_to_cart()

    # количество в корзине обновляется, но в самой корзине элемента нет, хотя выше ожидание на появление
    # элемента настроено. Поэтому time.sleep
    time.sleep(2)
    driver.find_element_by_link_text('Checkout »').click()
    print(cart_items_quantity)


    remove_item()









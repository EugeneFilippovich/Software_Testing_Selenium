import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


path_to_file = 'darkwing_duck_-_screenshot_-_h_-_2016.jpg'
# Вот здесь происходит очень странный join, но работает, что странно.
abs_path = '{}'.format(os.path.abspath(os.path.join(os.path.dirname(__file__), path_to_file)))
abs_path_new = abs_path.replace("\\", "\\\\")


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_12(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    def input_item_name(name):
        _item_name = name
        return _item_name

    def log_in():
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    log_in()

    left_box_menu = driver.find_element_by_id('box-apps-menu')
    left_box_items_links = left_box_menu.find_elements_by_tag_name('a')
    left_box_items_links[1].click()

    header = driver.find_element_by_id('content')
    buttons = header.find_elements_by_css_selector('[class = button]')
    buttons[1].click()

    tabs = driver.find_element_by_class_name('index')
    tabs_list = tabs.find_elements_by_tag_name('li')

    # general tab
    def general_tab_fill(name):
        content_general = driver.find_element_by_class_name('content')
        item_name = content_general.find_element_by_name('name[en]')
        radio = content_general.find_elements_by_css_selector('[type = radio')
        radio[0].click()
        item_name.send_keys(input_item_name(name))
        item_code = content_general.find_element_by_name('code')
        item_code.send_keys(31051993)
        input_wrapper = content_general.find_elements_by_class_name('input-wrapper')
        checkboxes = input_wrapper[2].find_elements_by_css_selector('[type = checkbox]')
        checkboxes[1].click()

        quantity = content_general.find_element_by_name('quantity')
        quantity.clear()
        quantity.send_keys(26)

        file_path = content_general.find_element_by_css_selector('[type = file]')
        file_path.send_keys(abs_path_new)

        date_from = content_general.find_element_by_name('date_valid_from')
        date_from.send_keys(31051993)
        date_to = content_general.find_element_by_name('date_valid_to')
        date_to.send_keys(26012020)

    # information tab
    def information_tab_fill():
        content_information = driver.find_element_by_class_name('content')
        manufacturer_id = Select(content_information.find_element_by_css_selector('[name = manufacturer_id]'))
        manufacturer_id.select_by_visible_text('ACME Corp.')

        keywords = content_information.find_element_by_css_selector('[name = keywords]')
        keywords.send_keys('Batman ink.')

        short_description = content_information.find_element_by_name('short_description[en]')
        short_description.send_keys('Limited')

        description_wrapper = content_information.find_element_by_class_name('trumbowyg-editor')
        description_wrapper.send_keys('No one can beat Batman')

        head_title = content_information.find_element_by_name('head_title[en]')
        head_title.send_keys('Darkwing Duck')

        meta_description = content_information.find_element_by_name('meta_description[en]')
        meta_description.send_keys('DRKWNG')

    # prices tab
    def prices_tab_fill():
        content_prices = driver.find_element_by_class_name('content')
        purchase_price = content_prices.find_element_by_name('purchase_price')
        purchase_price.clear()
        purchase_price.send_keys(26)

        currency = Select(content_prices.find_element_by_name('purchase_price_currency_code'))
        currency.select_by_visible_text('US Dollars')

        price_usd = content_prices.find_element_by_name('prices[USD]')
        price_usd.send_keys(26)

        price_euro = content_prices.find_element_by_name('prices[EUR]')
        price_euro.send_keys(22)

    def submit_item():
        buttons_set = driver.find_element_by_class_name('button-set')
        submit = buttons_set.find_element_by_css_selector('[type = submit]')
        submit.click()

    def check_item_appear(name):
        try:
            table = driver.find_element_by_class_name('dataTable')
            table.find_element_by_link_text(input_item_name(name))
            print('\nItem has been added successfully')
        except NameError:
            print('\nItem has not been added')


    general_tab_fill('Darkwing Duck')
    tabs_list[1].click()
    time.sleep(0.5)

    information_tab_fill()
    tabs_list[3].click()
    time.sleep(0.5)

    prices_tab_fill()

    submit_item()

    time.sleep(1)

    check_item_appear('Darkwing Duck')

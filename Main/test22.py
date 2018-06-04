import pytest
import os
from selenium import webdriver


path_to_file = 'Main/darkwing_duck_-_screenshot_-_h_-_2016.jpg'
abs_path = os.path.abspath(path_to_file)

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_12(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    def log_in():
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
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

    # general tab
    content = driver.find_element_by_class_name('content')
    item_name = content.find_element_by_name('name[en]')
    item_name.send_keys('Darkwing Duck')
    item_code = content.find_element_by_name('code')
    item_code.send_keys(31051993)
    input_wrapper = content.find_elements_by_class_name('input-wrapper')
    checkboxes = input_wrapper[2].find_elements_by_css_selector('[type = checkbox]')
    checkboxes[1].click()

    quantity = content.find_element_by_name('quantity')
    quantity.clear()
    quantity.send_keys(26)

    file_path = content.find_element_by_css_selector('[type = file]')
    file_path.send_keys(abs_path)

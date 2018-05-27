import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_7(driver):

    """
    :type driver: selenium.webdriver.Chrome
    """

    def log_in():
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    def check_heading(element, page):
        try:
            driver.find_element_by_tag_name(element)
        except Exception as E:
            print(E, "no h1 element found on the " + page)

    log_in()

    items_list = []

    left_box_menu = driver.find_element_by_id("box-apps-menu")
    left_box_items_links = left_box_menu.find_elements_by_tag_name('a')

    for item in left_box_items_links:
        items_list.append(item.get_attribute('href'))

    for item in items_list:
        driver.get(item)
        check_heading('h1', item)
        internal_items_list = []
        try:
            internal_items = driver.find_element_by_class_name("docs")
            internal_items_links = internal_items.find_elements_by_tag_name('a')
            if internal_items:
                for internal_item in internal_items_links:
                    internal_items_list.append(internal_item.get_attribute('href'))
                for _ in internal_items_list:
                    if _ in items_list:
                        pass
                    else:
                        driver.get(_)
                        check_heading('h1', _)
        except Exception:
            pass







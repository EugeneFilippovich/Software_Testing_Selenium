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

    items_list = []

    def log_in():
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    def get_items_list(menu_id, elements_tag):

        left_box_menu = driver.find_element_by_id(menu_id)
        left_box_items_links = left_box_menu.find_elements_by_tag_name(elements_tag)

        for link in left_box_items_links:
            items_list.append(link.get_attribute('href'))

    def get_internal_items_list(internal_items, internal_items_links):

        inherit_items = driver.find_element_by_class_name(internal_items)
        inherit_items_links = inherit_items.find_elements_by_tag_name(internal_items_links)
        if inherit_items:
            for inherit_items in inherit_items_links:
                internal_items_list.append(inherit_items.get_attribute('href'))
            for _ in internal_items_list:
                if _ in items_list:
                    pass
                else:
                    driver.get(_)
                    check_heading('h1', _)

    def check_heading(element, page):
        try:
            driver.find_element_by_tag_name(element)
        except Exception as E:
            print(E, "no h1 element found on the " + page)

    log_in()

    get_items_list("box-apps-menu", 'a')

    for item in items_list:
        driver.get(item)
        check_heading('h1', item)
        internal_items_list = []
        try:
            get_internal_items_list('docs', 'a')
        except Exception:
            pass







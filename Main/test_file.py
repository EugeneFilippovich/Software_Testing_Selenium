import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_9_2(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    countries_list_array = []
    not_null_zones_link = []

    def log_in():
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    log_in()

    table = driver.find_element_by_id("content")
    rows = table.find_elements_by_class_name('row')
    for row in rows:
        table_row = row.find_elements_by_tag_name("a")
        for _ in table_row:
            if _ in countries_list_array:
                pass
            else:
                countries_list_array.append(_)









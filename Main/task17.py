import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = {"browser": "ALL"}


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities=d)
    request.addfinalizer(wd.quit)
    return wd


def test_task_17(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    items_links = []

    def log_in():
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    log_in()

    table = driver.find_element_by_class_name('dataTable')
    links = table.find_elements_by_css_selector('tr:not(.header):not(.footer) > td:nth-of-type(5) > a:nth-of-type(1)')
    for link in links:
        items_links.append(link.get_attribute('href'))

    for _ in items_links:
        driver.get(_)
        for l in driver.get_log("browser"):
            print(l)

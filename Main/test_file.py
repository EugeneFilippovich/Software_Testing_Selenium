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

    def log_in():
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    log_in()

    table = driver.find_element_by_id("content")
    rows = table.find_elements_by_class_name('row')
    for row in rows:
        table_row = row.find_elements_by_tag_name('a')
        link = table_row[0].get_attribute('href')
        countries_list_array.append(link)

    for href in countries_list_array:
        zones_array = []
        driver.get(href)
        zones_table = driver.find_element_by_id("table-zones")
        zones = zones_table.find_elements_by_css_selector("tr:not(.header)")
        for _ in zones:
            try:
                double_ = _.find_elements_by_tag_name('td')
                elements = double_[2]
                zone_name = elements.find_element_by_css_selector('[selected = selected]')
                zones_array.append(zone_name.get_attribute('textContent'))
            except Exception:
                pass

        if zones_array == sorted(zones_array):
            print("\nZones for {} country sorted well".format(href))
        else:
            print("\nCheck your sorting for {} country".format(href))
        driver.back()










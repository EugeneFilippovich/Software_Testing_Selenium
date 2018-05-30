import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_9_1(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """
    countries_list_array = []
    not_null_zones_link = []

    def log_in():
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    log_in()

    #get countries list
    table_content = driver.find_element_by_class_name("dataTable")
    countries_list = table_content.find_elements_by_class_name("row")
    for country in countries_list:
        country_name = country.find_element_by_tag_name('a')
        country_link = country_name.get_attribute('href')
        countries_list_array.append(country_name.text)

        null_check = country.find_elements_by_tag_name('td')
        regions = null_check[5].get_attribute('textContent')

        if int(regions) != 0:
            not_null_zones_link.append(country_link)

    for link in not_null_zones_link:
        country_zones_array = []
        driver.get(link)
        country_zones_table = driver.find_element_by_id("table-zones")
        country_zones_list = country_zones_table.find_elements_by_css_selector("tr:not(.header)")
        for _ in country_zones_list:
            double_ = _.find_elements_by_tag_name('td')
            country_zones_array.append(double_[2].get_attribute('textContent'))

        filtered_country_zones_array = list(filter(None, country_zones_array))

        if filtered_country_zones_array == sorted(filtered_country_zones_array):
            print("\nWell done! Country zone list is sorted \n")
        else:
            print("\nOoops, your zones list for {} is NOT sorted!\n".format(link))

        print(filtered_country_zones_array)

        driver.back()


    #check sorted list
    filtered_countries_list_array = list(filter(None, countries_list_array))

    if filtered_countries_list_array == sorted(filtered_countries_list_array):
        print("\nWell done! Countries are sorted\n")
    else:
        print("\nOoops, your countries list is NOT sorted!\n")


    print(countries_list_array)


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













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
    country_zones_array = []
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

    for _ in not_null_zones_link:
        driver.get(_)
        country_zones_table = driver.find_element_by_id("table-zones")
        country_zones_list = country_zones_table.find_elements_by_css_selector("tr:not(.header)")
        for _ in country_zones_list:
            double_ = _.find_elements_by_tag_name('td')
            country_zones_array.append(double_[2].get_attribute('textContent'))

        driver.back()
        # for zone in country_zones_table:
        #     zone.find_elements_by_tag_name('tr')
        #     for zo

    #check sorted list
    filtered_countries_list_array = list(filter(None, countries_list_array))

    if filtered_countries_list_array == sorted(filtered_countries_list_array):
        print("Well done! Countries are sorted")
    else:
        print("Ooops, your countries list is NOT sorted!")

    filtered_country_zones_array = list(filter(None, country_zones_array))
    if filtered_country_zones_array == sorted(filtered_country_zones_array):
        print("Well done! Country zone list is sorted")
    else:
        print("Ooops, your zones list is NOT sorted!")




    print(filtered_countries_list_array)
    print(filtered_country_zones_array)










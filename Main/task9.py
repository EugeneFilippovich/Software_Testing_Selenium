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
        countries_list_array.append(country_name.text)

        null_check = country.find_elements_by_tag_name('td')
        regions = null_check[5].get_attribute('textContent')


        if int(regions) != 0:
            country_name.click()
            country_zones_table = driver.find_element_by_id("table-zones")
            country_zones_list = country_zones_table.find_elements_by_tag_name('tr')
            for _ in country_zones_list:
                _.find_elements_by_tag_name('td')
                country_zones_array.append(_.text)
            # for zone in country_zones_table:
            #     zone.find_elements_by_tag_name('tr')
            #     for zo

    #check sorted list

    if countries_list_array == sorted(countries_list_array):
        print("Well done! List is sorted")
    else:
        print("Ooops, your list is NOT sorted!")







    print(countries_list_array)
    print(country_zones_array)










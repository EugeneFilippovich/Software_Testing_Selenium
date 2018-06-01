import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_10(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """


    def log_in():
        driver.get("http://localhost/litecart/")

    log_in()

    category = driver.find_element_by_id("box-campaigns")
    item_link = category.find_element_by_class_name('link')

    # item name
    MP_item_name = item_link.find_element_by_class_name('name').get_attribute('textContent')

    # regular-price line text and price check
    MP_regular_price_font_line = item_link.find_element_by_tag_name("s").get_attribute('textContent')

    # regular-price color check
    MP_regular_price_color = driver.find_element_by_class_name('regular-price').value_of_css_property("color")

    # campaign-price strong text and price check
    MP_campaign_price_strong = item_link.find_element_by_tag_name("strong").get_attribute('textContent')

    # campaign-price color check
    MP_campaign_price_strong = driver.find_element_by_class_name('campaign-price').value_of_css_property("color")
    item_link.click()


    driver.get("http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1")

    item_box = driver.find_element_by_id('box-product')

    # item-page item name
    IP_item_name = item_box.find_element_by_class_name("title").get_attribute('textContent')

    # regular-price line text and price check
    IP_item_regular_price = item_box.find_element_by_tag_name("s").get_attribute('textContent')

    # regular-price color check
    IP_regular_price_color = driver.find_element_by_class_name('regular-price').value_of_css_property("color")

    # campaign-price strong text and price check
    IP_campaign_price_strong = item_box.find_element_by_tag_name("strong").get_attribute('textContent')

    # campaign-price color check
    IP_campaign_price_strong = driver.find_element_by_class_name('campaign-price').value_of_css_property("color")







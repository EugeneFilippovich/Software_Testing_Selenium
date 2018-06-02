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
    MP_price_wrapper = item_link.find_element_by_class_name('price-wrapper')

    # main-page item name
    MP_item_name = item_link.find_element_by_class_name('name').get_attribute('textContent')

    # regular-price line text and price check
    MP_regular_price_font_line = MP_price_wrapper.find_element_by_tag_name("s").get_attribute('textContent')

    # regular-price color check
    MP_regular_price_color = MP_price_wrapper.find_element_by_class_name('regular-price').value_of_css_property("color")

    # regular-price element size
    MP_regular_price_size = dict(MP_price_wrapper.find_element_by_class_name('regular-price').size)

    # campaign-price strong text and price check
    MP_campaign_price_strong = MP_price_wrapper.find_element_by_tag_name("strong").get_attribute('textContent')

    # campaign-price color check
    MP_campaign_price_strong = MP_price_wrapper.find_element_by_class_name('campaign-price').value_of_css_property("color")

    # campaign-price element size
    MP_campaign_price_size = dict(MP_price_wrapper.find_element_by_class_name('campaign-price').size)

    item_link.click()


    item_box = driver.find_element_by_id('box-product')
    IP_price_wrapper = item_box.find_element_by_class_name('price-wrapper')

    # item-page item name
    IP_item_name = item_box.find_element_by_class_name("title").get_attribute('textContent')

    # regular-price line text and price check
    IP_item_regular_price = IP_price_wrapper.find_element_by_tag_name("s").get_attribute('textContent')

    # regular-price color check
    IP_regular_price_color = IP_price_wrapper.find_element_by_class_name('regular-price').value_of_css_property("color")

    # regular-price element size
    IP_regular_price_size = dict(IP_price_wrapper.find_element_by_class_name('regular-price').size)

    # campaign-price strong text and price check
    IP_campaign_price_strong = IP_price_wrapper.find_element_by_tag_name("strong").get_attribute('textContent')

    # campaign-price color check
    IP_campaign_price_strong = IP_price_wrapper.find_element_by_class_name('campaign-price').value_of_css_property("color")

    # campaign-price element size
    IP_campaign_price_size = dict(IP_price_wrapper.find_element_by_class_name('campaign-price').size)


    def compare_names():
        if MP_item_name == IP_item_name:
            print('\nItem name on the main page and dedicated page is the same. Correct.')

    def compare_prices():
        if MP_regular_price_font_line == IP_item_regular_price:
            print('Regular price is same on both pages')

        if MP_campaign_price_strong == IP_campaign_price_strong:
            print('Campaign price is same on both pages')

    def check_reg_price_font_and_color():
        print('Price element with tag <s> was found. Element has {} color on the main page'
              ' and {} on the dedicated page. Correct.'.format(MP_regular_price_color, IP_regular_price_color))

    def check_campaign_price_font_and_color():
        print('Price element with tag <strong> was found. Element has {} color on the main page'
              ' and {} on the dedicated page. Correct.'.format(MP_campaign_price_strong, IP_campaign_price_strong))

    def compare_element_size():
        if MP_regular_price_size.get('height') < MP_campaign_price_size.get('height') and\
                        MP_regular_price_size.get('width') < MP_campaign_price_size.get('width'):
            print('Campaign price on the main page is larger than regular price. Correct')

        if IP_regular_price_size.get('height') < IP_campaign_price_size.get('height') and\
                        IP_regular_price_size.get('width') < IP_campaign_price_size.get('width'):
            print('Campaign price on the dedicated page is larger than regular price. Correct')


    compare_names()

    compare_prices()

    check_reg_price_font_and_color()

    check_campaign_price_font_and_color()

    compare_element_size()




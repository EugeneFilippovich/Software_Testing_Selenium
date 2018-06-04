import string
import random
import pytest
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

var = id_generator()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_10(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    driver.get("http://localhost/litecart/")


    def user_creation(_first_name, _second_name, _address, _postcode, _city, _country, _state, _phone, _password,):
        login_form = driver.find_element_by_css_selector('[name = login_form]')
        new_user = login_form.find_element_by_tag_name('a')
        new_user.click()

        registration_form = driver.find_element_by_css_selector('[name = customer_form')
        first_name = registration_form.find_element_by_name('firstname')
        second_name = registration_form.find_element_by_name('lastname')
        address_1 = registration_form.find_element_by_name('address1')
        postcode = registration_form.find_element_by_name('postcode')
        city = registration_form.find_element_by_name('city')
        country = Select(registration_form.find_element_by_css_selector('[name = country_code]'))
        zone_name = registration_form.find_elements_by_css_selector('[name = zone_code]')
        zone_state_province = Select(zone_name[1])
        email = registration_form.find_element_by_name('email')
        phone = registration_form.find_element_by_name('phone')
        desired_password = registration_form.find_element_by_name('password')
        confirm_password = registration_form.find_element_by_name('confirmed_password')
        create_account = registration_form.find_element_by_css_selector('[name = create_account')

        first_name.send_keys(_first_name)
        second_name.send_keys(_second_name)
        address_1.send_keys(_address)
        postcode.send_keys(_postcode)
        city.send_keys(_city)
        country.select_by_visible_text(_country)
        time.sleep(1)
        zone_state_province.select_by_visible_text(_state)
        email.send_keys(var + "@gmail.com")
        phone.send_keys(_phone)
        desired_password.send_keys(_password)
        confirm_password.send_keys(_password)
        create_account.click()



    def log_out():
        account_box = driver.find_element_by_id('box-account')
        list_items = account_box.find_elements_by_tag_name('li')
        logout = list_items[3].find_element_by_tag_name('a')
        logout.click()


    def log_in():
        login_form = driver.find_element_by_css_selector('[name = login_form]')
        log_in_email = login_form.find_element_by_css_selector('[name = email]')
        log_in_email.send_keys(var + "@gmail.com")
        log_in_password = login_form.find_element_by_css_selector('[name = password]')
        log_in_password.send_keys(123123)
        login_form.find_element_by_css_selector('[name = login]').click()


    user_creation('Eugene', 'Filippovich', 'Mihalova str.', 55555, 'Minsk', 'United States', 'California',
                  +375291112233, 123123)

    log_out()

    log_in()

    log_out()

import string
import random
import pytest
from selenium import webdriver


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


var = id_generator()

print(var)


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

    login_form = driver.find_element_by_css_selector('[name = login_form]')
    new_user = login_form.find_element_by_tag_name('a')
    new_user.click()

    registration_form = driver.find_element_by_css_selector('[name = customer_form')
    first_name = registration_form.find_element_by_name('firstname')
    second_name = registration_form.find_element_by_name('lastname')
    address_1 = registration_form.find_element_by_name('address1')
    postcode = registration_form.find_element_by_name('postcode')
    city = registration_form.find_element_by_name('city')
    country = registration_form.find_element_by_css_selector('[role = combobox]')
    zone_state_province = registration_form.find_element_by_name('zone_code')
    emain = registration_form.find_element_by_name('email')
    phone = registration_form.find_element_by_name('phone')
    desired_password = registration_form.find_element_by_name('password')
    confirm_password = registration_form.find_element_by_name('confirmed_password')

    first_name.send_keys('Eugene')
    second_name.send_keys('Filippovich')
    address_1.send_keys('Mihalova str.')
    postcode.send_keys(55555)
    city.send_keys('Minsk')
    emain.send_keys(var + "@gmail.com")
    phone.send_keys('375291112233')
    desired_password.send_keys(123123)
    confirm_password.send_keys(123123)
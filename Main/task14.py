import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_14(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    wait = WebDriverWait(driver, 10)


    def log_in():
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    log_in()

    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

    add_country = driver.find_element_by_css_selector('[class = button]')
    add_country.click()

    form = driver.find_element_by_tag_name('form')
    lines = form.find_elements_by_tag_name('tr')
    main_window = driver.current_window_handle
    main_window_title = driver.title
    html = driver.find_element_by_tag_name('html')
    for line in lines:
        try:
            a = line.find_element_by_css_selector('[target = _blank]')
            a.click()
            new_window = driver.window_handles[1]
            driver.switch_to.window(new_window)
            # есть использовать строку 49, то тест сразу же заканчивается на первом пробеге цикла. Почему?
            # wait.until(EC.presence_of_element_located(html))
            wait.until(EC.number_of_windows_to_be(2))
            new_window_title = driver.title
            if main_window_title != new_window_title:
                print('\nnew tab opened successfully')
            else:
                print('\nnew tab was NOT opened')
            print('Main window: {}. \tNew window: {}'.format(main_window_title, new_window_title))
            driver.close()
            driver.switch_to.window(main_window)
        except Exception:
            pass











import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_spyder(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    def log_in():
        driver.get('https://www.youtube.com/channel/UCQWeDEwQruA_CcyR08bIE9g/videos?disable_polymer=1')

    log_in()



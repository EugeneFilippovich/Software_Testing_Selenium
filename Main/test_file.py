import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


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

    def view_all_videos():
        for i in range(100):
            try:
                load_more = driver.find_element_by_css_selector('[class = load-more-text]')
                load_more.click()
                time.sleep(2)
            except:
                pass

    def get_all_videos_info():

        all_videos = driver.find_elements_by_css_selector('[class = yt-lockup-dismissable]')
        for i in all_videos:
            a = i.find_elements_by_tag_name('a')
            for _ in a:
                print(_.get_attribute('textContent'))

            view_count = i.find_elements_by_tag_name('li')
            for _ in view_count:
                print(_.get_attribute('textContent'))

    log_in()
    view_all_videos()
    get_all_videos_info()


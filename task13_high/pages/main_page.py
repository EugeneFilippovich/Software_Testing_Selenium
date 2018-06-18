

class MainPage:

    """
    :type driver: selenium.webdriver.Chrome
    """

    def __init__(self, driver):
        self.driver = driver

    def load_main_page(self):
        self.driver.get("http://localhost/litecart/")
        return self

    def select_item(self):
        most_popular = self.driver.find_element_by_id('box-most-popular')
        most_popular_items = most_popular.find_elements_by_class_name('link')
        most_popular_items[0].click()
        return self

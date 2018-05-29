import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_8(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """

    def find_stickers(main_box, content, list, list_items, item_link, image_wrapper, sticker_selector):
        category = driver.find_element_by_id(main_box)
        category_name_title = category.find_element_by_class_name('title')
        category_content = category.find_element_by_class_name(content)
        category_list = category_content.find_element_by_tag_name(list)
        category_list_items = category_list.find_elements_by_tag_name(list_items)
        for item in category_list_items:
            link = item.find_element_by_class_name(item_link)
            img_wrapper = link.find_element_by_class_name(image_wrapper)
            try:
                sticker = img_wrapper.find_elements_by_css_selector(sticker_selector)
                print((link.get_attribute("title") + " " + category_name_title.text + " " + "{}" + str(len(sticker)) + "{}")
                      .format(' has ', ' stickers'))

            except Exception as E:
                print("{}", "{}" + link.get_attribute("title") + "{}" + "{}" + category_name_title.text)\
                    .format(str(E), "no stickers found for the ", "item"," in the ")

    driver.get("http://localhost/litecart/en/")

    find_stickers('box-most-popular', 'content', 'ul', 'li', 'link', 'image-wrapper', "[class ^=sticker]")
    find_stickers('box-campaigns', 'content', 'ul', 'li', 'link', 'image-wrapper', "[class ^=sticker]")
    find_stickers('box-latest-products', 'content', 'ul', 'li', 'link', 'image-wrapper', "[class ^=sticker]")

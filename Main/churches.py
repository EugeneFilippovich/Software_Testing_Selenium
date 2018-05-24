# -- coding: utf-8 --
import pytest
from selenium import webdriver
import os

filename = "E:\\Emails\\links.txt"
filename2 = "E:\\Emails\\links2.txt"
filename3 = "E:\\Emails\\links3.txt"


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def get_links(link):
    with open(filename, 'a') as out:
        out.write(link + '\n')


def get_links2(link):
    with open(filename2, 'a') as out:
        out.write(link + '\n')


def get_links3(name, email):
    with open(filename3, 'a') as out:
        out.write(name + " " + email + '\n')


def test_email_parser(driver):
    """
    :type driver: selenium.webdriver.Chrome
    """
    driver.get("http://www.eglises.org/france/?Langue=en")
    list_column = driver.find_element_by_class_name("multicol")
    list_elements = list_column.find_elements_by_tag_name("li")
    for element in list_elements:
        link = element.find_element_by_tag_name("a")
        link_href = link.get_attribute("href")

        get_links(link_href)

    with open(filename) as f:
        lines = f.readlines()

        for line in lines:
            driver.get(line)
            bloc = driver.find_element_by_class_name("bloc-centre-2")
            churches = bloc.find_elements_by_tag_name("li")
            for _ in churches:
                link2 = _.find_element_by_tag_name("a")
                link2_href = link2.get_attribute("href")

                get_links2(link2_href)

    with open(filename2) as f2:
        lines2 = f2.readlines()

        for line2 in lines2:
            driver.get(line2)
            driver.execute_script("let acrs = document.querySelectorAll('acronym'); let acr_length = acrs.length; for(let i =0; i < acr_length; i++){ acrs[i].parentNode.removeChild(acrs[i]);}")
            church_name = driver.find_element_by_tag_name("h1")
            name = church_name.text
            if '\xc9' in name:
                name = name.replace('\xc9', 'E')
            else:
                name = church_name.text
            try:
                church_email = driver.find_element_by_partial_link_text("@")
                if (church_email.is_displayed()):
                    get_links3(name, church_email.text)
                else:
                    get_links3(name, "no email")
            except Exception:
                pass













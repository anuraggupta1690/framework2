"""
fixtures file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""

import pytest
from _pytest.fixtures import SubRequest

from lib.webdriver_instance import WebDriverInstance
from pageobjects.element_page_class import ElementPage
from pageobjects.home_page_class import HomePage


@pytest.fixture()
def get_driver(request: SubRequest):
    if hasattr(request, "param") and (request.param.get("browser") == "firefox" or
                                      request.param.get("browser") == "ff"):
        driver = WebDriverInstance.get_ff_driver_instance()
    else:
        driver = WebDriverInstance.get_chrome_driver_instance()
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(get_driver):
    home_page = HomePage(driver=get_driver)
    yield home_page


@pytest.fixture()
def get_element_page(get_driver):
    element_page = ElementPage(driver=get_driver)
    yield element_page

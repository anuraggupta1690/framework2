"""
fixtures file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""

import pytest
from _pytest.fixtures import SubRequest

from lib.webdriver_instance import WebDriverInstance
from pageobjects.alerts_page_class import AlertsPage
from pageobjects.book_page_class import BooksPage
from pageobjects.element_page_class import ElementPage
from pageobjects.home_page_class import HomePage
from pageobjects.interactions_page_class import InteractionPage
from pageobjects.widgets_page_class import WidgetsPage


@pytest.fixture()
def get_driver(request: SubRequest):
    """This fixture initialize the driver object"""
    if hasattr(request, "param") and (request.param.get("browser") == "firefox" or
                                      request.param.get("browser") == "ff"):
        driver = WebDriverInstance.get_ff_driver_instance()
    else:
        driver = WebDriverInstance.get_chrome_driver_instance()
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(get_driver):
    """This fixture initialize the HomePage object"""
    home_page = HomePage(driver=get_driver)
    yield home_page


@pytest.fixture()
def get_element_page(get_driver):
    """This fixture initialize the ElementPage object"""
    element_page = ElementPage(driver=get_driver)
    yield element_page


@pytest.fixture()
def get_alert_page(get_driver):
    """This fixture initialize the AlertsPage object"""
    alert_page = AlertsPage(driver=get_driver)
    yield alert_page


@pytest.fixture()
def get_widgets_page(get_driver):
    """This fixture initialize the WidgetsPage object"""
    widgets_page = WidgetsPage(driver=get_driver)
    yield widgets_page


@pytest.fixture()
def get_interaction_page(get_driver):
    """This fixture initialize the InteractionPage object"""
    element_page = InteractionPage(driver=get_driver)
    yield element_page


@pytest.fixture()
def get_book_page(get_driver):
    """This fixture initialize the BooksPage object"""
    book_page = BooksPage(driver=get_driver)
    yield book_page

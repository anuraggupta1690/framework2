"""
home_page_class file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class HomePage(BaseClass):
    """
    This is page object class for Home Page
    """
    element_page_icon = "//h5[contains(text(), 'Elements')]"
    form_page_icon = "//h5[contains(text(), 'Forms')]"
    alert_page_icon = "//h5[contains(text(), 'Alerts, Frame & Windows')]"
    widgets_page_icon = "//h5[contains(text(), 'Widgets')]"
    interation_page_icon = "//h5[contains(text(), 'Interactions')]"
    book_page_icon = "//h5[contains(text(), 'Book Store Application')]"

    def __init__(self, driver, url: str = URLs.base_url):
        super().__init__(driver, url)

    def get_icon(self, icon_name: str) -> WebElement:
        """
        This method open the page based on icon name like: 'element', 'form', 'alert', 'widgets', 'interation', 'book'
        :param str icon_name: Valid icon name mentioned above
        :return: Icon WebElement
        :rtype: WebElement
        """
        icon = getattr(HomePage, f"{icon_name}_page_icon")
        return self.driver.find_element(By.XPATH, icon)

    def click_on_icon(self, icon_name: str) -> None:
        """
        This method open the page based on icon name like: 'element', 'form', 'alert', 'widgets', 'interation', 'book'
        :param str icon_name: Valid icon name mentioned above
        :return: None
        :rtype: NoneType
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_icon(icon_name=icon_name))
        self.get_icon(icon_name=icon_name).click()

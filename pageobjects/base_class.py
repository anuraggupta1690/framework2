"""
Base Class file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""
from selenium.webdriver.common.by import By


class BaseClass:
    """
    This is a base class which contains all generic methods required by child page objects classes
    """
    header = "//div[@class = 'main-header']"

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def open_page(self):
        self.driver.get(self.url)

    def open_url(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def get_header(self):
        """
        This method return the header text
        :return:
        """
        return self.driver.find_element(By.XPATH, self.header).text


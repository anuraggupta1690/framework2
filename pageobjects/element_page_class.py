"""
element_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""
from selenium.webdriver.common.by import By

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class ElementPage(BaseClass):
    """
    This is Page Object class for Element page
    """
    text_box = ".text"
    full_name = "//input[@id='userName']"
    email = "//input[@id='userEmail']"
    current_address = "//textarea[@id='currentAddress']"
    permanent_address = "//textarea[@id='permanentAddress']"
    submit_button = "//button[@id='submit']"
    output_name = "#name"
    output_email = "#email"
    output_current_address = "p[id=currentAddress]"
    output_permanent_address = "p[id=permanentAddress]"

    def __init__(self, driver, url: str = URLs.elements_page):
        super().__init__(driver, url)

    def text_box_click(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_box).click()

    def enter_full_name(self, name):
        self.driver.find_element(By.XPATH, self.full_name).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email).send_keys(email)

    def enter_current_address(self, current_address):
        self.driver.find_element(By.XPATH, self.current_address).send_keys(current_address)

    def enter_permanent_address(self, permanent_address):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, self.permanent_address).send_keys(permanent_address)

    def submit(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()

    def get_text_value(self, element: str) -> str:
        """
        Method which return inner text of given element(like: name, email, current_address, permanent_address
        :param element: element name in text
        :return: Inner text of element
        :rtype: str
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR, getattr(self, f"output_{element}")).text

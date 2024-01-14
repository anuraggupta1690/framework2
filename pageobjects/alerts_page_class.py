"""
alerts_page_class file Designed by Anurag Gupta
 :date:  14-01-2024
 :author: Anurag Gupta
"""

from lib.constants import URLs
from pageobjects.base_class import BaseClass


class AlertsPage(BaseClass):
    """
    This is Page Object class for Alerts page
    """

    def __init__(self, driver, url: str = URLs.alert_page):
        super().__init__(driver, url)

"""
Webdriver Instance file Designed by Anurag Gupta
 :date:  07-01-2024
 :author: Anurag Gupta
"""

# Import the required modules
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as fs

from lib.logging_ import get_logger as logger_


class WebDriverInstance:

    @staticmethod
    def get_chrome_driver_instance(headless: bool = False):
        # Create an instance of ChromeOptions
        options = webdriver.ChromeOptions()
        logger_().info("Chrome Browser is invoked")
        if headless:
            options.add_argument("--headless")  # Open Chrome in headless mode
        # Add some arguments to the options
        options.add_argument("--start-maximized")  # Open Chrome in maximize mode
        options.add_argument("--incognito")  # Open Chrome in incognito mode
        options.add_argument("--disable-extensions")  # Disable existing extensions on Chrome browser
        options.add_argument("--disable-popup-blocking")  # Disable pop-ups displayed on Chrome browser
        options.add_argument("--version")  # Print chrome browser version

        # Pass the options and caps to the ChromeDriver constructor
        driver = webdriver.Chrome(options=options)
        logger_().info(f"Chrome Browser is invoked with options: {options}")
        return driver

    @staticmethod
    def get_ff_driver_instance(headless: bool = False):
        # Create an instance of FirefoxOptions
        options = webdriver.FirefoxOptions()
        logger_().info("Firefox Browser is invoked")
        if headless:
            options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        # Add some arguments to the options
        options.add_argument("--headless")  # Open Firefox in headless mode
        options.add_argument("--private")  # Open Firefox in private mode
        options.add_argument("--width=800")  # Set the window width
        options.add_argument("--height=600")  # Set the window height
        options.add_argument("--version")  # Print Firefox browser version
        logger_().info(f"Firefox Browser is invoked with options: {options}")
        return webdriver.Firefox(service=fs())

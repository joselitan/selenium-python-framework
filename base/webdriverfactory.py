"""
@package base

WebDriver Factory class implementation
It creates a webdriver intstance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser, website):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.website = website
    """
        Set chrome driver and iexplorer environment based on OS 
    """
    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return: 'WebDriver instance'
        """
        # baseURL = "https://test.viasat.se"
        baseURL = self.website
        if self.browser == 'firefox':
            binary = FirefoxBinary(r"C:\Users\vr320\AppData\Local\Mozilla Firefox\firefox.exe")
            driver = webdriver.Firefox(firefox_binary=binary)
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver

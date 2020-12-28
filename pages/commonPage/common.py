import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class CommonElementPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _cookie = ".//app-cookie-notice//button"

    def closeCookie(self):
        if self.getElement(self._cookie, locatorType="xpath"):
            self.ElementClick(self._cookie, locatorType="xpath")
        else:
            pass
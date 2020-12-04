import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class MailinatorPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _email = ".//input[@placeholder='Enter Public Mailinator Inbox']"
    _go_button = "go-to-public"
    _email_row = ".//tr[contains(@id,'row_sigmatest_st01_se')]/td/a" # Glömt ditt Viasat-lösenord på Mina Sidor

    def enter_email(self, data):
        self.SendKeys(data, self._email, locatorType="xpath")
        self.ElementClick(self._go_button)

    def click_email_row(self):
        self.ElementClick(self._email_row, locatorType="xpath")






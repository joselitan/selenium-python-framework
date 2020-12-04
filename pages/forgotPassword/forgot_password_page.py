import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class ForgotPasswordPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _email_field = ".//input[@placeholder='E-postadress']"
    _page_title = ".//h1"
    _success_msg = ".//a[@href='/registrera']/parent::p/preceding-sibling::p"
    _confirm_button = ".//button[contains(text(),' Bekräfta')]"
    _disabled_button = ".//button/@disabled"

    def confirm_button(self):
        if self._confirm_button:
            self.ElementClick(self._confirm_button, locatorType="xpath")
        else:
            self.isElementPresent(self._disabled_button)
            self.log.info("button is disabled")

    def enter_password(self, email):
        self.SendKeys(email, self._email_field, locatorType="xpath")

    # actions
    def request_new_password(self, email):
        self.enter_password(email)
        self.confirm_button()

    # validation
    def validate_page_title(self, text):
        page_title = self.getElement(self._page_title, locatorType="xpath").text
        result = self.verifyMatchingText(page_title, text)
        return result

    def validate_success_msg(self, text):
        sleep(.5)
        success_msg = self.getElement(self._success_msg, locatorType="xpath").text
        result = self.verifyPageContainsText(success_msg, text)
        return result
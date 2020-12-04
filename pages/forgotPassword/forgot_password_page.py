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
    # locator
    _email = ".//input[@placeholder='Enter Public Mailinator Inbox']"
    _go_button = "go-to-public"
    _email_row = ".//tr[contains(@id,'row_sigmatest_st01_se')]/td/a" # Glömt ditt Viasat-lösenord på Mina Sidor
    _change_password = "BYT LÖSENORD"

    def confirm_button(self):
        if self._confirm_button:
            self.ElementClick(self._confirm_button, locatorType="xpath")
        else:
            self.isElementPresent(self._disabled_button)
            self.log.info("button is disabled")

    def enter_password(self, email):
        self.SendKeys(email, self._email_field, locatorType="xpath")

    def enter_email(self, email):
        self.driver.get("https://www.mailinator.com/")
        self.SendKeys(email, self._email, locatorType="xpath")
        self.ElementClick(self._go_button, locatorType="linktext")

    def click_email_row(self):
        self.ElementClick(self._email_row, locatorType="xpath")

    def click_on_activationLink(self):
        self.switchToFrame(id="msg_body")
        self.ElementClick(self._change_password, locatorType="xpath")


    # actions
    def request_new_password(self, email):
        """

        :param email: Email inserted through Viasat FE
        :return:
        """
        self.enter_password(email)
        self.confirm_button()

    def enter_forgot_password(self, email):
        """

        :param email: Email inserted through the mailinator FE
        :return:
        """
        self.enter_email(email)
        self.click_email_row()
        self.click_on_activationLink()


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
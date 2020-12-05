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
    _password = ".//input[@placeholder='Lösenordet behöver vara minst 8 tecken långt, varav minst 1 siffra']"
    _confirm_password = ".//input[@placeholder='Bekräfta lösenord']"
    _page_title = ".//h1"
    _success_msg = ".//a[@href='/registrera']/parent::p/preceding-sibling::p"
    _confirm_button = ".//button[contains(text(),' Bekräfta')]"
    _disabled_button = ".//button/@disabled"
    _password_restored = ".//span[contains(@class,'icon-check')]/following-sibling::p"

    # locator
    def confirm_button(self):
        if self._confirm_button:
            self.ElementClick(self._confirm_button, locatorType="xpath")
        else:
            self.isElementPresent(self._disabled_button)
            self.log.info("button is disabled")

    def enter_email(self, email):
        self.SendKeys(email, self._email_field, locatorType="xpath")

    def enter_password(self, password):
        self.SendKeys(password, self._password, locatorType="xpath")

    def enter_confirm_password(self, confirmPassword):
        self.SendKeys(confirmPassword, self._confirm_password, locatorType="xpath")


    # actions
    def request_new_password(self, email):
        """
        :param email: Email inserted through Viasat FE
        :return:
        """
        self.enter_email(email)
        self.confirm_button()

    #def enter_new_password(self, email="", password ="", confirmPassword=""):
    def enter_new_password(self, password="", confirmPassword=""):
        #self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirmPassword)
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

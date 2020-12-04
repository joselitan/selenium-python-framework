import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class RegistrationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _reg_customer = ".//input[@placeholder='Kundnummer']"
    _reg_ssn = ".//input[@placeholder='Personnummer (ÅÅÅÅMMDDXXXX)']"
    _reg_email = ".//input[@placeholder='E-postadress']"
    _reg_password = ".//input[@type='password']"
    _reg_confirm_password = ".//input[@placeholder='Bekräfta lösenord']"
    _confirm_button = ".//button[contains(text(),' Bekräfta')]"
    _disabled = ".//button/@disabled"
    _customer_exist_alert = ".//p[contains(text(), 'Ange ditt kundnummer')]/following-sibling::mat-form-field/div//mat-error[@role='alert']"
    _email_exist_alert = ".//p[contains(text(), 'E-postadress')]/following-sibling::mat-form-field/div//mat-error[@role='alert']"
    _general_alert = ".//mat-error"
    _cookie = ".//app-cookie-notice//button"


    def closeCookie(self):
        if self.getElement(self._cookie, locatorType="xpath"):
            self.ElementClick(self._cookie, locatorType="xpath")
        else:
            pass

    def enter_customerNr(self, customerID):
        self.SendKeys(customerID, self._reg_customer, locatorType="xpath")

    def enter_ssn(self, ssn):
        self.SendKeys(ssn, self._reg_ssn, locatorType="xpath")

    def enter_email(self, email):
        self.SendKeys(email, self._reg_email, locatorType="xpath")

    def enter_password(self, password):
        self.SendKeys(password, self._reg_password, locatorType="xpath")

    def enter_confirm_password(self, confirmPassword):
        self.SendKeys(confirmPassword, self._reg_confirm_password, locatorType="xpath")

    def confirm_button(self):
        if self._confirm_button:
            self.ElementClick(self._confirm_button, locatorType="xpath")
        else:
            self.isElementPresent(self._disabled)
            self.log.info("button is disabled")

    # actions
    def registerCustomer(self, customerID="", ssn="", email="", password="", confirmPassword=""):
        self.enter_customerNr(customerID)
        self.enter_ssn(ssn)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirmPassword)
        self.confirm_button()
        sleep(0.5)

    def customer_error_msg(self, text):
        sys_error = self.getElement(self._customer_exist_alert, locatorType="xpath").text
        #self.log.info(sys_error)
        error = self.verifyMatchingText(sys_error, text)
        return error

    def email_error_msg(self, text):
        sys_error = self.getElement(self._email_exist_alert, locatorType="xpath").text
        #self.log.info(sys_error)
        error = self.verifyMatchingText(sys_error, text)
        return error

    def general_error_msg(self, text):
        sys_error = self.getElement(self._general_alert, locatorType="xpath").text
        self.log.info(sys_error)
        error = self.verifyPageContainsText(sys_error, text)
        return error

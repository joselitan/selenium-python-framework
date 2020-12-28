import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_icon = "//div[@class='icon-user-black']"
    _login_link = "//span[@class='action-button bold']"
    _email_password_button = ".//div[@class='section login-options']/button[2]"
    _email_field = "//input[@placeholder='E-postadress']"
    _password_field = "//input[@placeholder='Ange lösenord']"
    _login_button = "//button[@class='peach-button is-sm']"
    _shopping_bag = "//div[@class='icon-shopping-bag']"
    # _shopping_bag = "icon-shopping-bag"
    _login_failed = "//mat-error[@role='alert']"
    _email_required = ".//mat-error[@class='mat-error ng-star-inserted']"
    _password_required = ".//mat-error[@class='mat-error ng-tns-c93-17 ng-star-inserted']"
    _mat_error = "//mat-error[@id='mat-error-2']"
    _email_password_list = ".//form/div/mat-form-field/div/div/following-sibling::div/following-sibling::div/div/mat-error"
    _forgot_password = ".//u[starts-with(text(),'Har du glömt ditt lösenord')]/parent::a"

    ##### Element calls

    def clickLoginIcon(self):
        self.ElementClick(self._login_icon, locatorType="xpath")

    def clickLoginLink(self):
        self.ElementClick(self._login_link, locatorType="xpath")

    def clickEmailPasswordButton(self):
        self.ElementClick(self._email_password_button, locatorType="xpath")

    def enterEmail(self, email):
        self.SendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.SendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        # self.waitForElement(self._login_button, locatorType="xpath",)
        self.ElementClick(self._login_button, locatorType="xpath")

    def backspaceEmail(self):
        self.BackspaceElement(self._email_field, locatorType="xpath")

    def backspacePassword(self):
        self.BackspaceElement(self._password_field, locatorType="xpath")

    ##### Functions Calls

    def login_popup(self):
        self.clickLoginIcon()
        self.clickLoginLink()
        self.clickEmailPasswordButton()

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        sleep(3)

    def enter_invalid_email(self, email ="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)

    def clearfields(self):
        self.backspaceEmail()
        self.backspacePassword()
        sleep(3)

    ##### Validation

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._shopping_bag, locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._login_failed, locatorType="xpath")
        return result

    def verifyErrorMsg(self):
        result = self.getText(self._mat_error, locatorType="xpath")
        return self.verifyPageContainsText(result, "Det angivna användarnamnet eller lösenordet är felaktigt.")

    def verifyEmailRequired(self):
        result = self.getText(self._email_required, locatorType="xpath")
        return self.verifyPageContainsText(result, "E-postadress krävs")

    def verifyPasswordRequired(self):
        result = self.getText(self._password_required, locatorType="xpath")
        return self.verifyPageContainsText(result, "Lösenord krävs")

    def verifyInvalidEmailMsg(self):
        result = self.getText(self._email_required, locatorType="xpath")
        return self.verifyPageContainsText(result, "E-postadressen måste vara giltig")

    def return_attribute(self):
        message_attribute = self.driver.find_elements_by_xpath( ".//form/div/mat-form-field/div/div/following-sibling::div/following-sibling::div/div/mat-error")
        for row in message_attribute:
            print(row.get_attribute("class"))

    def verify_forgot_msg(self, text):
        error_msg = self.getElement(self._forgot_password, locatorType="xpath").text
        result = self.verifyPageContainsText(error_msg, text)
        return result




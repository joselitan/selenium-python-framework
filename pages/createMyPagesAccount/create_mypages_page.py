import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class CreateAccount(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ##### Lcators
    _popup_button = "//button[@class='peach-button is-sm ng-tns-c258-0']"
    _list_of_fields = ".//form/div/div/mat-form-field/div/div/div/input"
    # _list_error_msg = ".//form/div/div/mat-form-field/div/div/following-sibling::div/following-sibling::div/div/mat-error"
    _list_error_msg = ".//mat-error"
    _page_title = ".//h1"
    _kundnummer = ".//input[@placeholder = 'Kundnummer']"
    _ssn = ".//input[@placeholder = 'Personnummer (ÅÅÅÅMMDDXXXX)']"
    _email = ".//input[@placeholder = 'E-postadress']"
    _password = ".//input[@placeholder = 'Ska vara minst 8 tecken och 1 siffra långt']"
    _confirm_password = "//input[@placeholder = 'Bekräfta lösenord']"
    _submit_button = ".//button[@class='outline-button is-sm']"
    # _customer_required = ".//mat-error"
    _customer_required = ".//mat-error[@class='mat-error ng-tns-c168-4 ng-star-inserted']"
    # _customer_required = ".//mat-error[contains(text(),' Kundnummer krävs ')]"
    # _ssn_required = ".//mat-error[contains(text(),' Personnummer krävs ')]]"
    _ssn_required = ".//mat-error"
    _email_required = ".//mat-error[contains(text(),' E-postadress krävs ')]"
    _password_required = ".//mat-error[contains(text(),' Lösenord krävs ')]"
    _require_same_password = ".//mat-error[@class='mat-error ng-star-inserted']"


    ##### Element calls

    def closeCookiePopup(self):
        self.ElementClick(self._popup_button, locatorType="xpath")

    def enterCustomerNumber(self, customeNr):
        self.SendKeys(customeNr, self._kundnummer, locatorType="xpath")

    def enterSSN(self, ssn):
        self.SendKeys(ssn, self._ssn, locatorType="xpath")

    def enterEmail(self, email):
        self.SendKeys(email, self._email, locatorType="xpath")

    def enterPassword(self, password):
        self.SendKeys(password, self._password, locatorType="xpath")

    def enterConfirmPassword(self, conpassword):
        self.SendKeys(conpassword, self._confirm_password, locatorType="xpath")

    def clickSubmitButton (self):
        self.ElementClick(self._submit_button, locatorType="xpath")

    def showList(self):
        self.getElements(self._list_error_msg, locatorType="xpath")

    # def show

    def retrieveClassAttribute(self):
        self.getAttribute_class(self._customer_required, locatorType="xpath")



    ##### Function calls

    def create_mypages_account(self, customerNumber, ssn, email, password, conpassword):
        self.enterCustomerNumber(customerNumber)
        self.enterSSN(ssn)
        self.enterEmail(email)
        self.enterPassword(password)
        self.enterConfirmPassword(conpassword)
        # self.clickSubmitButton()

    def create_mypages_account_messages(self, customerNumber, ssn, email, password, conpassword):
        self.closeCookiePopup()
        self.enterCustomerNumber(customerNumber)
        self.enterSSN(ssn)
        self.enterEmail(email)
        self.enterPassword(password)
        self.enterConfirmPassword(conpassword)

    def clearfields(self):
        self.BackspaceElement(self._kundnummer, locatorType="xpath")
        self.BackspaceElement(self._ssn, locatorType="xpath")
        self.BackspaceElement(self._email, locatorType="xpath")
        self.BackspaceElement(self._password, locatorType="xpath")
        self.BackspaceElement(self._confirm_password, locatorType="xpath")

    ##### validation

    def verifyTitlePage(self):
        page_title = self.getText(self._page_title, locatorType="xpath")
        return self.verifyPageContainsText(page_title, "Aktivera Mina Sidor-konto")

    def verifyAlertCustomer(self):
        customer_required = self.getText(self._customer_required, locatorType="xpath")
        # customer_required = self.getElement(self._customer_required, locatorType="xpath")
        return self.verifyPageContainsText(customer_required, "Kundnummer krävs")

    def verifyAlertSSN(self):
        ssn_required = self.getText(self._ssn_required, locatorType="xpath")
        # ssn_required = self.getElement(self._ssn_required, locatorType="xpath")
        return self.verifyPageContainsText(ssn_required, 'Personnummer krävs')

    def verifyAlertEmail(self):
        email_required = self.getText(self._email_required, locatorType="xpath")
        # email_required = self.getElement(self._email_required, locatorType="xpath")
        return self.verifyPageContainsText(email_required, 'E-postadress krävs')

    def verifyAlertPassword(self):
        password_required = self.getText(self._email_required, locatorType="xpath")
        # password_required = self.getElement(self._password_required)
        return self.verifyPageContainsText(password_required, 'Lösenord krävs')

    def verifyAlertConfirmPassword(self):
        confirmed_password_reguired = self.getText(self._email_required, locatorType="xpath")
        return self.verifyPageContainsText(confirmed_password_reguired, 'Lösenord krävs')

    def verifyAlertSamePassword(self):
        same_password = self.getText(self._require_same_password, locatorType="xpath")
        print("#######", same_password, "#######")
        return self.verifyPageContainsText(same_password, 'Lösenorden behöver vara samma')

    def return_attributes(self):
        # message_attribute = self.getElement(self._email_password_list, locatorType="xpath")
        message_attribute = self.driver.find_elements_by_xpath(".//form/div/div/mat-form-field/div/div/following-sibling::div/following-sibling::div/div/mat-error")

        for row in message_attribute:
            print(row.get_attribute("class"))

    def get_attribute_x(self):
        message_attribute = self.getAttribute_class(self._customer_required, locatorType="xpath")
        print("#######")
        print("#######")
        print(message_attribute)

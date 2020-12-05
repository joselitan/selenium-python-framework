import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage
import re

class MailinatorPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _email = ".//input[@placeholder='Enter Public Mailinator Inbox']"
    _go_button = "go-to-public"
    _email_row = ".//tr[contains(@id,'row_sigmatest_st01_se')]/td/a" # Glömt ditt Viasat-lösenord på Mina Sidor
    _url = "/html/body/div/section/p[3]"
    _change_password = "BYT LÖSENORD"


    def enter_email(self, email):
        sleep(.5)
        self.driver.get("https://www.mailinator.com/")
        sleep(.9)
        self.SendKeys(email, self._email, locatorType="xpath")
        self.ElementClick(self._go_button)

    def click_email_row(self):
        self.ElementClick(self._email_row, locatorType="xpath")

    def click_on_activationLink(self):
        self.switchToFrame(id="msg_body")
        self.ElementClick(self._change_password, locatorType="linktext")
        self.switchToDefaultContent()

    def retrieve_url(self):
        self.switchToFrame(id="msg_body")
        url = self.getElement(self._url, locatorType="xpath").text
        url_string = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', url)
        return ''.join([str(elem) for elem in url_string])

    def navigate_to_reset_page(self):
        url = self.retrieve_url()
        self.driver.get(url)

    # actions
    def enter_forgot_password(self, email):
        self.enter_email(email)
        self.click_email_row()
        # self.click_on_activationLink()
        self.navigate_to_reset_page()

    #def enter_reset_password(self):






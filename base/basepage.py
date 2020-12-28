"""
@package base
(view lesson 185. BasePage and Util concept instructions on udemy)
Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title
        :param titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyPageContainsText(self, actualTitle, titleToVerify):
        """
        Verify the page Title
        :param titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = actualTitle
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page text")
            print_stack()
            return False

    def verifyMatchingText(self, actualText, textToVerify):
        """
        :param actualText:
        :param textToVerify:
        :return:
        """
        try:
            actualText = actualText
            return self.util.verifyTextMatch(actualText, textToVerify)
        except:
            self.log.error("Failed to get match text")
            print_stack()
            return False

    def verifyMatchingNumbers(self, actualNumber, numberToVerify):
        """
        :param actualNumber:
        :param numberToVerify:
        :return:
        """
        try:
            actual = actualNumber
            # print("verify Matching numbers: Actual", actual, "type", type(actual))
            # print("verify Matching numbers: numberToVerify", numberToVerify, "type", type(numberToVerify))
            return self.util.verifySumMatch(actual, numberToVerify)
        except:
            self.log.error("Failed to get match sum")
            print_stack()
            return False
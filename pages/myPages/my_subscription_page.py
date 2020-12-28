import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage
import re

class MySubscription(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _app_subscription_panel = ".//app-subscription-panel"
    _app_add_tv = ".//app-add-tv"
    _edit_button = ".//button[contains(@class,'wide')]/span[contains(text(),'Ändra')]"
    _add_box = ".//button[contains(@class,'add-hardware')]"
    # _price_package = ".//span[contains(text(),' {}')]/parent::div/following-sibling::div[contains(@class,'product-price')]/span[1]"
    _price_package = ".//span/parent::div/following-sibling::div[contains(@class,'product-price')]/span[1]"
    _sum_panel = ".//div[contains(@class,'sum')]/strong"

    _underline_button = ".//button[contains(@class,'underline-button-arrow')]"
    _alert_container = ".//div[contains(@class,'alert-container')]/p"
    _question_filled = ".//span[contains(@class,'icon-question-filled')]"
    _question_remove = ".//span[contains(@class,'icon-remove')]"


    def get_sum_of_individual_channel(self):
        """
        Loops through prices of individual channels
        :return: the sum total of all individual prices
        """
        price_packages = self.getElements(locator=self._price_package, locatorType="xpath")
        price_list = []
        for price in price_packages:
            price = float(price.text)
            price_list.append(price)
        return sum(price_list)

    def click_expandable_button(self):
        self.ElementClick(locator=self._underline_button, locatorType="xpath")

    # verification
    def verifyPageSubPanel(self):
        result = self.isElementPresent(locator=self._app_subscription_panel, locatorType="xpath")
        return result

    def verifyPageAddTV(self):
        result = self.isElementPresent(locator=self._app_add_tv, locatorType="xpath")
        return result

    def verifyEditButton(self):
        result = self.isElementPresent(locator=self._edit_button, locatorType="xpath")
        return result

    def verifyAddBoxButton(self):
        result = self.isElementPresent(locator=self._add_box, locatorType="xpath")
        return result

    def verifyPackagePrice(self, mainPackage):
        price_package = self.getElement(locator=self._price_package.format(mainPackage), locatorType="xpath").text
        return float(price_package)

    def verifySumPackagePanel(self):
        sum_panel = self.getElement(locator=self._sum_panel, locatorType="xpath").text
        tot_sum_channel = self.get_sum_of_individual_channel()
        return self.verifyMatchingNumbers(sum_panel, "{}".format(tot_sum_channel))

    def verifyExpandableButton(self):
        return self.isElementPresent(locator=self._underline_button, locatorType="xpath")

    def verifyAlertText(self):
        return self.isElementPresent(locator=self._alert_container, locatorType="xpath")

    def verifyQuestionFill(self):
        """
        check if question icon is visible
        :return:
        """
        return self.isElementPresent(locator=self._question_filled, locatorType="xpath")

    def verifyQuestionRemove(self):
        """
        check if question icon remove button is visible
        """
        return self.isElementPresent(locator=self._question_remove, locatorType="xpath")

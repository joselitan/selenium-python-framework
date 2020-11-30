import time
import utilities.customer_logger as cl
import logging
from base.basepage import BasePage

class TVGuidePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _epg_left_arrow = ".//span[ @class ='epg-left-arrow']"
    _epg_left_right = ".//span[@class='epg-right-arrow']"
    _epg_select_header = ".//div[@class='epg-select-header']/span"
    _epg_triangle_arrow = ".//div[@class='epg-select-header']/span[contains(@class,'epg-triangle-arrow')]"
    _epg_categories_list = ".//ul[@class='epg-categories-list']/li"
    _epg_current_date = ".//span[contains(@class,'epg-triangle-arrow')]/preceding-sibling::span"
    #_epg_dropdown = ".//div[@class='epg-select']//div[@class='epg-dropdown']/span[contains(text(),'{}')]"
    #_epg_dropdown = ".//div[@class='epg-select']"
    _epg_dropdown = ".//div[@class='epg-select']//div[@class='epg-dropdown']/span[{}]"
    _cookie = ".//app-cookie-notice//button"


    def closeCookie(self):
        self.ElementClick(self._cookie, locatorType="xpath")

    def selectTVGuidebyDate(self, value):
        """
        :param value: value between 1 - 10
        :return:
        """
        self.ElementClick(self._epg_triangle_arrow, locatorType="xpath")
        self.ElementClick(locator=self._epg_dropdown.format(value), locatorType="xpath")
        time.sleep(3)

    # Action
    def selectDate(self, value):
        self.selectTVGuidebyDate(value)

    # validation
    def verify_current_date(self):
        result = self.isElementDisplayed(self._epg_current_date, locatorType="xpath")
        return result

    def verify_match_text(self, textToVerify):
        date = self.getElement(self._epg_current_date, locatorType="xpath").text
        result =  self.verifyMatchingText(date, textToVerify)
        return result
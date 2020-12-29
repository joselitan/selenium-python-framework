import utilities.customer_logger as cl
import logging
from base.basepage import BasePage
import datetime
from datetime import date
from datetime import datetime, date, time, timedelta


class SummerhousePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _from_date = ".//div[contains(@class,'datepickers')]/div[1]/div[@class='form']/button"
    _to_date = ".//div[contains(@class,'datepickers')]/div[2]/div[@class='form']/button"
    _select_date = ".//tbody/tr[@role='row']/td[@aria-label='{}']"
    _current_date = ".//tbody[@role='grid']/tr[@role='row']/td[@aria-selected='true']"

    def click_from_date(self):
        self.ElementClick(self._from_date, locatorType="xpath")

    def click_to_date(self):
        self.ElementClick(self._to_date, locatorType="xpath")

    def get_from_date(self):
        today = str(date.today())
        return today

    def selectFromDate(self):
        today = self.get_from_date()
        self.ElementClick(locator=self._select_date.format(today), locatorType="xpath")

    def get_to_date(self):
        date_new = self.get_from_date() + datetime.timedelta(2)
        return date_new

    def selectToDate(self):
        date_forward = self.get_to_date()
        self.ElementClick(locator=self._select_date.format(date_forward))

    # actions
    def applyFromDate(self):
        self.click_from_date()
        self.selectFromDate()

    def applyToDate(self):
        self.click_to_date()
        self.selectToDate()
from pages.loginfunc.login_page import LoginPage
from pages.myPages.my_subscription_page import MySubscription
from pages.myPages.viasat_summerhouse_page import SummerhousePage
from pages.commonPage.common import CommonElementPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SummerhouseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ms = MySubscription(self.driver)
        self.shp = SummerhousePage(self.driver)
        self.ts = Status(self.driver)
        self.cep = CommonElementPage(self.driver)

    # @pytest.mark.run(order=1)
    def test_summerhouse_request(self):
        self.cep.closeCookie()
        self.lp.login_popup()
        self.lp.login("jlmm83@hotmail.com", "test1234")
        self.shp.applyFromDate()
        self.shp.applyToDate()
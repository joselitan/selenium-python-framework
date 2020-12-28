from pages.loginfunc.login_page import LoginPage
from pages.myPages.my_subscription_page import MySubscription
from pages.commonPage.common import CommonElementPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MypagesSubscription(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ms = MySubscription(self.driver)
        self.ts = Status(self.driver)
        self.cep = CommonElementPage(self.driver)

    # @pytest.mark.run(order=1)
    def test_mySubscription_landing(self):
        self.cep.closeCookie()
        self.lp.login_popup()
        self.lp.login("jlmm83@hotmail.com", "test1234")
        result = self.ms.verifyPageSubPanel()
        self.ts.mark(result, "subscription panel visible")
        result2 = self.ms.verifyEditButton()
        self.ts.mark(result2, "edit button visible")
        result3 = self.ms.verifyAddBoxButton()
        self.ts.mark(result3, "add box button visible")
        result6 = self.ms.verifySumPackagePanel()
        self.ts.mark(result6, "sum is valid")
        resultx = self.ms.verifyPageAddTV()
        self.ts.markFinal(self.test_mySubscription_landing.__name__, resultx, "verify TV section")

    def test_underline_button(self):
        result = self.ms.verifyExpandableButton()
        self.ts.mark(result, "Expandable is visible")
        self.ms.click_expandable_button()
        result1 = self.ms.verifyQuestionFill()
        self.ts.mark(result1, "Question icon is visible")
        result2 = self.ms.verifyQuestionRemove()
        self.ts.mark(result2, "Question remove icon is visible")
        resultx = self.ms.verifyAlertText()
        self.ts.markFinal(self.test_underline_button.__name__, resultx, "verify text exist")


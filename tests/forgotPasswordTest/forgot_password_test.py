from selenium import webdriver
from pages.forgotPassword.forgot_password_page import ForgotPasswordPage
from pages.registerPage.registration_page import RegistrationPage
from pages.mailinatorPage.mailinator_page import MailinatorPage
from utilities.status import Status
from param import param_se
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")

class ForgotResetPassword(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.fpp = ForgotPasswordPage(self.driver)
        self.rp = RegistrationPage(self.driver)
        self.mp = MailinatorPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_forgot_password(self):
        self.rp.closeCookie()
        # sigmatest_se_82231423@mailinator.com
        # sigmatest_st01_se_82609197@mailinator.com
        self.fpp.request_new_password("sigmatest_st01_se_82609197@mailinator.com")
        result = self.fpp.validate_page_title("Begär nytt lösenord")
        self.ts.mark(result, "title is successful")
        result2 = self.fpp.validate_success_msg(param_se.return_message)
        self.ts.mark(result2, "success msg")

    @pytest.mark.run(order=2)
    def test_get_activation_mail(self):
        self.mp.enter_forgot_password("sigmatest_st01_se_82609197@mailinator.com")

    @pytest.mark.run(order=3)
    def test_reset_password(self):
        with open (r"C:\Users\vr320\websitePO\confirmation_code.txt") as in_file:
            for code in in_file:
                print("text" + code + "text")
                self.fpp.enter_new_password(code=code,password="test1234", confirmPassword="test1234")
        #result = self.fpp.validate_password_restored("Ditt lösenord har återställts. Nu kan du logga in.")
        #self.ts.markFinal("test_reset_password", result, "final test was successful")
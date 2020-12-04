from selenium import webdriver
from pages.forgotPassword.forgot_password_page import ForgotPasswordPage
from pages.registerPage.registration_page import RegistrationPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ForgotResetPassword(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.fpp = ForgotPasswordPage(self.driver)
        self.rp = RegistrationPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_forgot_password(self):
        self.rp.closeCookie()
        self.fpp.request_new_password("test_3@test.com")
        result = self.fpp.validate_page_title("Begär nytt lösenord")
        self.ts.mark(result, "title is successful")
        result2 = self.fpp.validate_success_msg("Vi har nu skickat instruktioner om hur du återställer ditt lösenord till test_3@test.com.")
        self.ts.mark(result2, "success msg")

    def test_get_activation_mail(self):
        pass

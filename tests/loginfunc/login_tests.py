from selenium import webdriver
from pages.loginfunc.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves toaceEmail() the next test method

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login_popup()
        self.lp.login("jlmm83@hotmail.com", "test123")
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, "error message doesn't exist")
        #result2 = self.lp.verifyErrorMsg()
        #self.ts.markFinal("test_invalidLogin", result, "error does text not visible")

    @pytest.mark.run(order=2)
    def test_empty_field_error_msg(self):
        self.lp.clearfields()
        email_required = self.lp.verifyEmailRequired()
        self.ts.mark(email_required, "email required msg exist")
        password_required = self.lp.verifyPasswordRequired()
        self.ts.mark(password_required, "email required mesg exists")
        # self.ts.markFinal("test_empty_field_error_msg", password_required, "password required msg doesn't exist")

    @pytest.mark.run(order=3)
    def test_invalid_email(self):
        self.lp.enter_invalid_email("jlmm83...", "test123")
        email_invalid_msg = self.lp.verifyInvalidEmailMsg()
        self.ts.mark(email_invalid_msg, "invalid required msg doesn't exist")
        self.ts.markFinal("test_invalid_email", email_invalid_msg, " invalid required email msg doesn't exist")


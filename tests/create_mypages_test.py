from selenium import webdriver
from pages.createMyPagesAccount.create_mypages_page import CreateAccount
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateAccountTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ca = CreateAccount(self.driver)
        self.ts = Status(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves toaceEmail() the next test method

    # @pytest.mark.run(order=4)
    # def test_create_account(self):
    #     page_title = self.ca.verifyTitlePage()
    #     self.ts.mark(page_title, "title doesn't exist")
    #     self.ca.create_mypages_account("123", "123121", "email@email.com", "test12345", "test12345")
    #     #self.ca.return_attribute()

    @pytest.mark.run(order=1)
    def test_fill_form_fields(self):
        page_title = self.ca.verifyTitlePage()
        self.ts.mark(page_title, "title doesn't exist")
        self.ca.create_mypages_account_messages("123", "123121", "email@email.com", "test12345", "test12345")

    @pytest.mark.run(order=2)
    def test_validate_field_msg(self):
        self.ca.clearfields()



    @pytest.mark.run(order=3)
    def test_verify_password(self):
        self.ca.create_mypages_account_messages("123", "199012121212", "email@email.com", "test12345", "test1234")
        self.ca.return_attributes()
        same_password_required = self.ca.verifyAlertSamePassword()
        self.ts.mark(same_password_required, "Required same password not visible")








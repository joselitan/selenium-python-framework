from selenium import webdriver
from pages.registerPage.registration_page import RegistrationPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegistrationPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_registration_customer_exist(self):
        self.rp.closeCookie()
        self.rp.registerCustomer("82222568", "198304221073", "jose.martin@allente.tv", "test1234", "test1234")
        result = self.rp.customer_error_msg("Ett konto med det angivna kundnumret finns redan")
        self.ts.mark(result, "error customerId msg visible")

    @pytest.mark.run(order=2)
    def test_registration_email_exist(self):
        self.rp.registerCustomer(customerID="82222562", email="jose.martin@allente.tv")
        result2 = self.rp.email_error_msg("E-postadressen är redan registrerad.")
        #self.ts.mark(result2, "error email msg visible")
        self.ts.markFinal("test_registration_page", result2, "succesful")

    @pytest.mark.run(order=3)
    def test_registration_ssn_exist(self):
        self.rp.registerCustomer(customerID="82637416", ssn="198304221073", email="jose.martin@allente.se")
        result3 = self.rp.general_error_msg("Vi kan inte hitta ett aktivt abonnemang kopplat till")
        self.ts.mark(result3, "error email msg visible")
        #self.ts.markFinal("test_registration_page", result3, "succesful")

    @pytest.mark.run(order=4)
    def test_registration_unequal_password(self):
        self.rp.registerCustomer(customerID="82637416", ssn="198304221073", email="jose.martin@allente.tv",
                                 password="test1234", confirmPassword="test12345")
        result4 = self.rp.general_error_msg("Lösenorden behöver vara samma")
        self.ts.markFinal("Last test case 'test_registration_unequal_password'", result4, "error unequal msg successful")
from pages.comparisonPage.comparison_page import ComparisonPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ComparisonTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = ComparisonPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_comparison_premium_page(self):
        self.cp.closeCookie()
        self.cp.navigatePackageSection("Premium")
        result = self.cp.verify_page_title("Tv-paket Premium")
        self.ts.mark(result, "verifying title")
        self.driver.back()

    @pytest.mark.run(order=2)
    def test_comparison_stor_page(self):
        self.cp.navigatePackageSection("Stor")
        result2 = self.cp.verify_page_title("Tv-paket Stor")
        self.ts.mark(result2, "Verifying title")
        self.driver.back()

    @pytest.mark.run(order=3)
    def test_comparison_mellan_page(self):
        self.cp.navigatePackageSection("Mellan")
        result3 = self.cp.verify_page_title("Tv-paket Mellan")
        self.ts.mark(result3, "Verifying title")
        self.driver.back()

    @pytest.mark.run(order=4)
    def test_comparison_bas_page(self):
        self.cp.navigatePackageSection("Bas")
        result4 = self.cp.verify_page_title("Tv-paket Bas")
        self.ts.markFinal("final test case", result4, "verifying title")

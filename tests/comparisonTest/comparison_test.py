from pages.comparisonPage.comparison_page import ComparisonPage
from utilities.status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ComparisonTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = ComparisonPage(self.driver)
        self.ts = Status(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves toaceEmail() the next test method

    # @pytest.mark.run(order=1)
    # def test_comparison_package(self):
    #     self.cp.closeCookie()
    #     self.cp.GoToPackageAndTab("Stor", "Viaplay")
    #     result = self.cp.verify_comparison_title()
    #     self.ts.mark(result, "verify package title")
    #     result2 = self.cp.verify_comparison_description()
    #     self.ts.mark(result2, "Verify package description")
    #
    # @pytest.mark.run(order=2)
    # def test_comparison_package2(self):
    #     self.cp.GoToPackageAndTab("Bas","Playtjänster")
    #     result = self.cp.verify_comparison_title()
    #     self.ts.mark(result, "verify package title")
    #     result2 = self.cp.verify_comparison_description()
    #     self.ts.markFinal("Test_comparison_nave", result2, "verify package description")
    #

    @pytest.mark.run(order=2)
    def test_comparison_page(self):
        # self.cp.closeCookie()
        self.cp.GoToPackageAndTab("Stor", "Tv-kanaler")
        result = self.cp.verify_comparison_title()
        self.ts.mark(result, "verify package title")
        result2 = self.cp.verify_comparison_description()
        self.ts.mark(result2, "verify package title")
        self.cp.openAllLogos()
        self.ts.markFinal("Test_comparison_nave", result2, "verify package description")

    # @pytest.mark.run(order=1)
    # def test_comparison_page_all(self):
    #     self.cp.closeCookie()
    #     self.cp.openAllPackagesTabsAndLogos()
    #

from pages.comparisonPage.comparison_page import ComparisonPage
from utilities.status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ComparisonTestsCSV(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = ComparisonPage(self.driver)
        self.ts = Status(self.driver)


    @pytest.mark.run(order=1)
    @data(*getCSVData(r"C:\Users\vr320\websitePO\testdata.txt"))
    @unpack
    def test_comparison_addon_section(self, section, title):
        self.cp.closeCookie()
        self.cp.navigateAddonSection(section)
        result = self.cp.verify_page_title(title)
        self.ts.mark(result, "confirming title")
        self.ts.markFinal("test comparison add section", result, "verification completed")
        self.driver.back()

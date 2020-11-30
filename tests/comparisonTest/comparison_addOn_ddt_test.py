from pages.comparisonPage.comparison_page import ComparisonPage
from utilities.status import Status
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ComparisonTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = ComparisonPage(self.driver)
        self.ts = Status(self.driver)


    @pytest.mark.run(order=1)
    @data(("V series & film", "V series & film"),
          ("V sport", "V sport"),
          ("C More Sport", "C More Sport"))
    @unpack
    def test_comparison_addon_section(self, section, title):
        self.cp.closeCookie()
        self.cp.navigateAddonSection(section)
        result = self.cp.verify_page_title(title)
        self.ts.mark(result, "confirming title")
        self.driver.back()

    # @pytest.mark.run(order=2)
    # def test_comparison_addon_vsport(self):
    #     self.cp.navigateAddonSection("V sport")
    #     result2 = self.cp.verify_page_title("V sport")
    #     self.ts.mark(result2, "confirming title")
    #     self.driver.back()
    #
    # @pytest.mark.run(order=3)
    # def test_comparison_addon_cmore(self):
    #     self.cp.navigateAddonSection("C More Sport")
    #     result3 = self.cp.verify_page_title("C More Sport")
    #     self.ts.markFinal("final test", result3, "final confirmation")

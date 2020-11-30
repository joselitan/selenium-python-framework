from pages.comparisonPage.trash.comparison_page import ComparisonPage
from utilities.status import Status
import unittest
import pytest


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
    # def test_comparison_nav(self):
    #     # self.cp.login_popup()
    #     self.cp.clickThroughComparisonPackages()
    #     # verify that each main package contains channels
    #
    # @pytest.mark.run(order=2)
    # def test_comparison_premium_length(self):
    #     self.cp.checkPremiumPackage()
    #     # assert amount of main packages
    #
    # @pytest.mark.run(order=3)
    # def test_open_channel(self):
    #     self.cp.openChannel()
    #     # verify content in openned channel
    #     result = self.cp.verify_channel_content()
    #     assert result == True

    # @pytest.mark.run(order=4)
    # def test_open_channels(self):
    #     self.cp.openAllPremiumChannels()
    #     self.cp.openAllStorChannels()
    #     self.cp.openAllMellanChannels()
    #     self.cp.openAllBasChannels()


    # @pytest.mark.run(order=5)
    # def test_clickable_list(self):
    #     self.cp.getClickableChannels()

    @pytest.mark.run(order=6)
    def test_open_channel_in_tabs (self):
        self.cp.clickOnStorAndTab("Playtjänster")
        result = self.cp.verify_comparison_title()
        self.ts.mark(result, 'verifying title')
        result2 = self.cp.verify_comparison_description()
        #self.ts.mark(result2, 'Verify description')


        self.ts.markFinal("Status", result2, "Verify description")

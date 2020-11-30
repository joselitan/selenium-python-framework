from pages.TVGuidePage.TVGuide_page import TVGuidePage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TvGuide(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.tvg = TVGuidePage(self.driver)
        self.ts = Status(self.driver)


    @pytest.mark.run(order=1)
    def test_tvguide_dropdown(self):
        self.tvg.closeCookie()
        self.tvg.selectTVGuidebyDate("3")
        result = self.tvg.verify_current_date()
        self.ts.mark(result, "verify dropdown contains selected sysdate")
        result2 = self.tvg.verify_match_text("Idag 28 november")
        self.ts.mark(result2, "verify that date matches")
        self.ts.markFinal("final test", result2, "sysdate verified")
import time

import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage

class ComparisonPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _premium_package = ".//button//comparison-package//h1[contains(text(),'Premium')]"
    _stor_package = ".//button//comparison-package//h1[contains(text(),'Stor')]"
    _mellan_package = ".//button//comparison-package//h1[contains(text(),'Mellan')]"
    _bas_package = ".//button//comparison-package//h1[contains(text(),'Bas')]"
    _channel = ".//comparison-channel-list/div//comparison-channel//img[@alt='TV3 ']"
    _close_button = ".//div[contains(@class,'expanded')]//div[@class='comparison-close-icon']"
    _channel_format = ".//comparison-channel-list/div//comparison-channel//img[@alt='{0}']"
    _channel_title = ".//div[contains(@class,'comparison-channels-title')]"
    _channel_description = ".//div[contains(@class,'comparison-channels-description')]"

    _cookie = ".//app-cookie-notice//button"
    _clickable_logos = ".//comparison-channel-list//div[@class='comparison-channel-container']/div[contains(@class,'clickable')]/img"
    _comparison_channels_title = ".//div[contains(@class,'comparison-channels-title')]"
    _comparison_tabs_filters = ".//comparison-tabs-filters//button"
    _comparison_tabs_filters_2 = ".//comparison-tabs-filters//button[contains(@class,'comparison-tab-button') and contains(text(),'{}')]"

    _channels_in_package = ".//div[contains(@class,'comparison-current-channel')]//comparison-channel/div/div/img"
    _main_packages = ".//button//comparison-package//h1[contains(text(),'')]"

    def closeCookie(self):
        self.ElementClick(self._cookie, locatorType="xpath")

    def clickOnPremium(self):
        self.ElementClick(self._premium_package, locatorType="xpath")

    def clickOnStor(self):
        self.ElementClick(self._stor_package, locatorType="xpath")

    def clickOnMellan(self):
        self.ElementClick(self._mellan_package, locatorType="xpath")

    def clickOnBas(self):
        self.ElementClick(self._bas_package, locatorType="xpath")

    def clickChannel(self):
        self.scrollIntoView(self._channel, locatorType="xpath")
        self.ElementClick(self._channel, locatorType="xpath")
        time.sleep(3)

    def closeChannel(self):
        self.waitForElement(self._close_button, locatorType="xpath")
        self.ElementClick(self._close_button, locatorType="xpath")

    def getMainPackages(self):
        list_main_package = []
        channel_amount = self.getElements(self._main_packages, locatorType="xpath")
        for channel in channel_amount:
            # print(channel.text)
            list_main_package.append(channel.text)
        self.log.info(list_main_package)
        return len(list_main_package)

    def getClickableChannels(self):
        """
        :return: list of clickable channels
        """
        # time.sleep(3)
        list_clickable_channels = []
        Clickable_channels = self.getElements(self._clickable_logos, locatorType="xpath")
        for clickable_channel in Clickable_channels:
            clickable_channel = clickable_channel.get_attribute('alt')
            list_clickable_channels.append(clickable_channel)
        return list_clickable_channels

    def clickThroughComparisonPackages(self):
        self.closeCookie()

        self.clickOnPremium()
        assert self.verify_channel_list() == True
        self.clickOnStor()
        assert self.verify_channel_list() == True
        self.clickOnMellan()
        assert self.verify_channel_list() == True
        self.clickOnBas()
        assert self.verify_channel_list() == True

    def checkPremiumPackage(self):
        self.clickOnPremium()
        self.getMainPackages()

    def openChannel(self):
        self.clickChannel()

    def tabFilters(self):
        tab_filter_buttons = self.getElements(self._comparison_tabs_filters, locatorType="xpath")
        return tab_filter_buttons

    def openAllPremiumChannels(self):
        self.closeCookie()

        channel_list = self.getClickableChannels()
        for channel in channel_list:
            import time
            time.sleep(0.5)
            self.scrollIntoView(locator=self._channel_format.format(channel), locatorType="xpath")
            self.ElementClick(locator=self._channel_format.format(channel), locatorType="xpath")
            assert self.isElementDisplayed(self._channel_title, locatorType="xpath") == True
            assert self.isElementDisplayed(self._channel_description, locatorType="xpath") == True
        self.scrollIntoView(self._comparison_channels_title, locatorType="xpath")

    def openAllPremiumTabs(self):
        """
        :return: Idea is to scroll through the channel icons on each tab filter
        """
        self.closeCookie()
        comparison_tabs_filter = self.tabFilters()
        exclude_first_tab = comparison_tabs_filter[1:]
        for click_button in exclude_first_tab:
            self.ElementClick(element=click_button)
            time.sleep(2)

    def openAllStorTab(self):
        """
        :return: Idea is to scroll through the channel icons on each tab filter
        """
        self.closeCookie()
        self.clickOnStor()
        comparison_tabs_filter = self.tabFilters()
        exclude_first_tab = comparison_tabs_filter[1:]
        for click_button in exclude_first_tab:
            self.ElementClick(element=click_button)
            time.sleep(2)

    def clickOnTab(self, tab):
        """
        :param tab: selected Tv kanaler, Playtjänster, Viaplay
        :return:
        """
        self.scrollIntoView(locator=self._comparison_tabs_filters_2.format(tab), locatorType="xpath")

        if tab == "Tv kanaler":
            self.ElementClick(locator=self._comparison_tabs_filters_2.format(tab), locatorType="xpath")
        elif tab == "Playtjänster":
            self.ElementClick(locator=self._comparison_tabs_filters_2.format(tab), locatorType="xpath")
            time.sleep(2)
        elif tab == "Viaplay":
            self.ElementClick(locator=self._comparison_tabs_filters_2.format(tab), locatorType="xpath")
            time.sleep(2)
        else:
            self.log.error("Tab doesn't exist")

    def openAllStorChannels(self):

        self.clickOnStor()

        channel_list = self.getClickableChannels()
        for channel in channel_list:
            import time
            time.sleep(0.5)
            self.scrollIntoView(locator=self._channel_format.format(channel), locatorType="xpath")
            self.ElementClick(locator=self._channel_format.format(channel), locatorType="xpath")
            assert self.isElementDisplayed(self._channel_title, locatorType="xpath") == True
            assert self.isElementDisplayed(self._channel_description, locatorType="xpath") == True
        self.scrollIntoView(self._comparison_channels_title, locatorType="xpath")

    def openAllMellanChannels(self):

        self.clickOnMellan()

        channel_list = self.getClickableChannels()
        for channel in channel_list:
            import time
            time.sleep(0.5)
            self.scrollIntoView(locator=self._channel_format.format(channel), locatorType="xpath")
            self.ElementClick(locator=self._channel_format.format(channel), locatorType="xpath")
            assert self.isElementDisplayed(self._channel_title, locatorType="xpath") == True
            assert self.isElementDisplayed(self._channel_description, locatorType="xpath") == True
        self.scrollIntoView(self._comparison_channels_title, locatorType="xpath")

    def openAllBasChannels(self):

        self.clickOnBas()

        channel_list = self.getClickableChannels()
        for channel in channel_list:
            import time
            time.sleep(0.5)
            self.scrollIntoView(locator=self._channel_format.format(channel), locatorType="xpath")
            self.ElementClick(locator=self._channel_format.format(channel), locatorType="xpath")
            assert self.isElementDisplayed(self._channel_title, locatorType="xpath") == True
            assert self.isElementDisplayed(self._channel_description, locatorType="xpath") == True
        self.scrollIntoView(self._comparison_channels_title, locatorType="xpath")

    def clickableChannels(self):
        self.clickOnBas()
        time.sleep(2)
        assert self.verify_channel_list() == True
        self.getClickableChannels()

    def clickOnStorAndTab(self, tab):
        self.clickOnStor()
        self.clickOnTab(tab)


    ##validation
    def verify_channel_list(self):
        result = self.isElementPresent(self._channels_in_package, locatorType="xpath")
        return result

    def verify_channel_content(self):
        result = self.isElementPresent(".//div[@class='comparison-channel-title']", locatorType="xpath")
        return result

    def verify_comparison_title(self):
        result = self.isElementDisplayed(self._channel_title, locatorType="xpath")
        return result

    def verify_comparison_description(self):
        result = self.isElementDisplayed(self._channel_description, locatorType="xpath")
        return result
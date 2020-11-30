import time
import utilities.customer_logger as cl
import logging
from base.basepage import BasePage

class ComparisonPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators package button
    _package_button = ".//button//comparison-package//h1[contains(text(),'{0}')]"
    _premium_package = ".//button//comparison-package//h1[contains(text(),'Premium')]"
    _stor_package = ".//button//comparison-package//h1[contains(text(),'Stor')]"
    _mellan_package = ".//button//comparison-package//h1[contains(text(),'Mellan')]"
    _bas_package = ".//button//comparison-package//h1[contains(text(),'Bas')]"
    _package_list = ".//mat-button-toggle-group//button//h1"
    _package_list_h1 = ".//mat-button-toggle-group//button//h1[contains(text(), '{}')]"
    _show_more_button = ".//h1[contains(text(),'{}')]/parent::div/following-sibling::div//button"
    _show_package_button = ".//div[@class='comparison-package-description']/h1[contains(text(),'{}')]/following-sibling::div/following-sibling::div//comparison-button"

    # Locators tabs
    _comparison_tab = ".//comparison-tabs-filters//button[contains(@class,'comparison-tab-button')]"
    _comparison_tab_channels = ".//comparison-tabs-filters//button[contains(@class,'comparison-tab-button') and contains(text(),'{0}')]"
    _close_button = ".//div[contains(@class,'expanded')]//div[@class='comparison-close-icon']"
    _channel_format = ".//comparison-channel-list/div//comparison-channel//img[@alt='{0}']"
    _comparison_title = ".//div[contains(@class,'comparison-channels-title')]"
    _comparison_channel_title = ".//div[@class='comparison-channel-title']"
    _comparison_description = ".//div[contains(@class,'comparison-channels-description')]"
    _comparison_channel_description = ".//div[@class='comparison-channel-description']"
    _clickable_logos = ".//comparison-channel-list//div[@class='comparison-channel-container']/div[contains(@class,'clickable')]/img"

    # addon view
    _comparison_addons_list = ".//div[contains(@class,'comparison-addons-list')]/comparison-addon"

    _cookie = ".//app-cookie-notice//button"


    def closeCookie(self):
        if self.getElement(self._cookie, locatorType="xpath"):
            self.ElementClick(self._cookie, locatorType="xpath")
        else:
            pass

    def clickOnPremium(self):
        self.ElementClick(self._premium_package, locatorType="xpath")

    def clickOnStor(self):
        self.ElementClick(self._stor_package, locatorType="xpath")

    def clickOnMellan(self):
        self.ElementClick(self._mellan_package, locatorType="xpath")

    def clickOnBas(self):
        self.ElementClick(self._bas_package, locatorType="xpath")


    def clickPackageButton(self, package):
        self.ElementClick(locator=self._package_button.format(package), locatorType="xpath")

    def clickTvTabChannel(self, tab):
        self.scrollIntoView(self._comparison_tab_channels.format(tab), locatorType="xpath")
        self.ElementClick(locator=self._comparison_tab_channels.format(tab), locatorType="xpath")

    def getClickablePackages(self):
        """
        :return: list of clickable packages
        """
        list_clickable_packages = []
        clickable_packages = self.getElements(self._package_list, locatorType="xpath")
        for packages in clickable_packages:
            list_clickable_packages.append(packages.text)
        return list_clickable_packages[::-1]

    def getClickableTabs(self):
        """
        :return: list of clickable tabs
        """
        list_clickable_tabs = []
        clickable_tabs = self.getElements(self._comparison_tab, locatorType="xpath")
        for tab in clickable_tabs:
            list_clickable_tabs.append(tab.text)
        return list_clickable_tabs[::-1]

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

    def getComparisonAddonList(self):
        """
        :return: list of clickable show more button
        """
        self.scrollIntoView(self._comparison_addons_list, locatorType="xpath")
        list_of_show_button = self.getElements(self._comparison_addons_list, locatorType="xpath")
        return list_of_show_button

    def clickOnAddonTab(self, name):
        """
        :param title: Entering title for addon compparison addon
        :return:
        """
        self.scrollIntoView(self._comparison_addons_list, locatorType="xpath")
        self.ElementClick(locator=self._show_more_button.format(name), locatorType="xpath")

    def clickOnPackageButton(self, name):
        # self.ElementClick(locator=self._show_package_button.format(name), locatorType="xpath")
        self.ElementDoubleClick(locator=self._show_package_button.format(name), locatorType="xpath")

    #######Calls############

    def openAllPackagesTabsAndLogos(self):

        packages = self.getClickablePackages()
        for package in packages:
            self.ElementClick(self._package_list_h1.format(package), locatorType="xpath")
            tabs = self.getClickableTabs()
            for tab in tabs:
                self.ElementClick(self._comparison_tab_channels.format(tab), locatorType="xpath")
                self.openAllLogos()

    def openAllLogos(self):

        channel_list = self.getClickableChannels()
        for channel in channel_list:
            import time
            time.sleep(0.2)
            self.scrollIntoView(locator=self._channel_format.format(channel), locatorType="xpath")
            self.ElementClick(locator=self._channel_format.format(channel), locatorType="xpath")
            assert self.isElementDisplayed(self._comparison_channel_title, locatorType="xpath") == True
            assert self.isElementDisplayed(self._comparison_channel_description, locatorType="xpath") == True
        self.scrollIntoView(self._comparison_title, locatorType="xpath")

    def GoToPackageAndTab(self, package, tab):
        self.clickPackageButton(package)
        self.clickTvTabChannel(tab)

    def openAllPremiumChannels(self):
        self.closeCookie()
        channel_list = self.getClickableChannels()
        for channel in channel_list:
            import time
            time.sleep(0.2)
            self.scrollIntoView(locator=self._channel_format.format(channel), locatorType="xpath")
            self.ElementClick(locator=self._channel_format.format(channel), locatorType="xpath")
            assert self.isElementDisplayed(self._comparison_title, locatorType="xpath") == True
            assert self.isElementDisplayed(self._comparison_description, locatorType="xpath") == True
        self.scrollIntoView(self._comparison_title, locatorType="xpath")

    def navigateAddonSection(self, name):
        self.clickOnAddonTab(name)

    def navigatePackageSection(self, name):

        self.clickOnPackageButton(name)
        #self.util.sleep(2, info="sleeping time")


    ######Validation########
    def verify_comparison_title(self):
        result = self.isElementPresent(self._comparison_title, locatorType="xpath")
        return result

    def verify_comparison_description(self):
        result = self.isElementPresent(self._comparison_description, locatorType="xpath")
        return result

    def verify_page_title(self, title):
        return self.verifyPageTitle(title)

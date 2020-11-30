from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.customer_logger as cl
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import os

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Ocurred")
            print_stack()

    def getTitle(self):
        # title = self.driver.title
        # print(title)
        return self.driver.title

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("'The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text element " + info)
            print_stack()
            text = None
        return text


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def getElements(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def getAttribute_class(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Attribute with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not with Attribute: " + locator + " and locatorType: " + locatorType)
        return element.get_attribute("class")

    def get_list_element(self, locator, locatorType="id"):
        element_list = []
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
            for i in element:
                element_list.append(i)
            return element_list
        except:
            self.log.info("Element not with Attribute: " + locator + " and locatorType: " + locatorType)
            return False
                

    def ElementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element  -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def ElementDoubleClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            action_chains = ActionChains(self.driver)
            action_chains.double_click(element).perform()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def SendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys  to element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("Sent on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def BackspaceElement(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            length = len(element.get_attribute("value"))
            element.send_keys(length * Keys.BACKSPACE)
            self.log.info("Backspacing text on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot backspace text on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def selectDropdownList(self, locator, locatorType="id"):

        """
        :param text: Element in dropdown list
        :param locator:
        :param locatorType:
        :param element:
        :return:
        """
        try:
            element = Select(self.getElement(locator, locatorType))
            element.select_by_visible_text("30 november")
            self.log.info("selected element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot select element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("###Element with locator: " + locator + " and locatorType: " + locatorType + " is present")
            else:
                self.log.info("###Element not found with locator: " + locator + " and locatorType: " + locatorType)
            return True
        except:
            self.log.info("###Element not found with locator: " + locator + " and locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.info("Element not found")

    def elementPresentCheck(self, locator, locatorType):
        try:
            elementList = self.getElement(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):

        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def scrollIntoView(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("window.scrollBy(0, -400);")
            self.log.info("Element found with locator: " + locator + " locatorType: " + locatorType)
            time.sleep(0.5)
        except:
            self.log.info("Element not found with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id       - id of iframe
                2. name     - name of iframe
                3. index    - index of iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to_frame(id)
        elif name:
            self.driver.switch_to_frame(name)
        else:
            self.driver.swtich_to_frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content

        Paremeters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to_default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of attribute of the element

        Parameters:
            1. Required:
                1. Attribute - attribute whose value to find
            2. Optional:
                1. element          - Element whose attribute need to find
                2. locator          - Locator of the element
                3. locatorType      - LocatorType to find the element
        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
            self.log.info("Element found with locator: " + locator + " locatorType: " + locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator (id(default), xpath, css, classname, linktext)
                2. info - Information about the element, label/name of the element
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found ")
        return enabled
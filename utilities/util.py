"""


Util class implementation
All most commonly  used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utilities.customer_logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        :param length: Length of string, number of characters string should have
        :param type: Type of characters string should have. Default is letters
        provide lower/upper/digits fo different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemlength=None):
        """
        Get a list of valid email ids

        :param listSize: Number of names. Default is 5 names in a list
        :param itemlength: It should be a list containing number of items equal to the listSize
                            This determines the length of the each item in the list
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemlength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualList: actualText
        :param expectedList: expectedText
        """
        self.log.info("Actual text From Application Web UI --> :: " + actualText)
        self.log.info("Expected text from Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION CONTAINS DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        :param actualList: actualText
        :param expectedList: expectedText
        """
        self.log.info("Actual text From Application Web UI --> :: " + actualText)
        self.log.info("Expected text from Application Web UI --> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION CONTAINS DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
        :param expectedList:
        :param actualList:
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        parameters:
            expectedList: Expected List
            actualList: actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True

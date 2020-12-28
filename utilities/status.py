"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point_markFinal("Test Name", result, "Message")
"""
from base.selenium_driver import SeleniumDriver
import utilities.customer_logger as cl
import logging

class Status(SeleniumDriver):


    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits CheckPointn class
        """
        #TestStatus.__test__ = False
        super(Status, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName +  " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
            self.log.info("===================================================================================")
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
            self.log.info("===================================================================================")



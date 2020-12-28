import utilities.customer_logger as cl
import logging
from time import sleep
from base.basepage import BasePage
import re

class VerifySum(BasePage):

    def check_sum(self):
        t = 5
        t2 = 6
        t3 = 11

        sum = t + t2

        return self.verifyMatchingNumbers(sum, t3)


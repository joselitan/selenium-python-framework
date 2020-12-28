
def verifyListContains(expectedList, actualList):
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

expectedList = [6,7,8,9,10]
actualList = [1,2,3,4,5]
print(verifyListContains(expectedList, actualList))




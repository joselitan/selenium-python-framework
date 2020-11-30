import csv

def getCSVData(filename):
    # create an empty list to store rows
    rows = []
    # Open the CSV file
    dataFile = open(filename, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from the reader list
    for row in reader:
        rows.append(row)
    return rows

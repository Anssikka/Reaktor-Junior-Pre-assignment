from csv import reader
from Modules.package import Package
import sys
sys.path.insert(0, '')

class Parser:
    def __init__(self, path):
        file = open(path, encoding="utf8")
        readPackages = reader(file)
        statusRows = list(readPackages)
        # Get only required rows.
        filterWords = ["Package:", "Description:", "Depends:"]
        illegalWord = "Pre-Depends:"
        cleanedRows = []
        for row in statusRows:
            if filterWords[0] in str(row) or filterWords[1] in str(row) or filterWords[2] in str(row) and not illegalWord in str(row):
                cleanedRows.append(str(row))

        # Make tuples out of the packages for easier processing.
        tuples = []
        while (len(cleanedRows) > 0):
            if "Package:" in cleanedRows[0]:
                tempList = []
                tempList.append(cleanedRows.pop(0))
                while (True):
                    if len(cleanedRows) <= 0:
                        break
                    if "Package:" in cleanedRows[0]:
                        tuples.append(tuple(tempList))
                        break
                    else:
                        tempList.append(cleanedRows.pop(0))

        # Turn Tuples into Package objects.
        self.packages = [Package(tupleVar) for tupleVar in tuples]
        self.generateDependants()

    def generateDependants(self):
        for package in self.packages:
            package.findDependants(self.packages)

    def getPackages(self):
        return self.packages


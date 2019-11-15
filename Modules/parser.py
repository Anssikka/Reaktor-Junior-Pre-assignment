from csv import reader
from Modules.package import Package
import sys
sys.path.insert(0, '')

class Parser:
    def __init__(self, path):
        #read the status.real file
        file = open(path, encoding="utf8")
        readPackages = reader(file)
        packagesAsRowList = list(readPackages)
        # Get only required rows.
        cleanedRows = self.cleanStatusReal(packagesAsRowList)
        # Make tuples out of the packages for easier processing.
        packageTuples = self.makeTuplesFromCleanedRows(cleanedRows)
        # Turn Tuples into Package objects.
        self.packages = [Package(tupleVar) for tupleVar in packageTuples]
        self.generateDependants()

    def cleanStatusReal(self, unCleanedRows):
        # Remove all unnecessary lines.
        cleanedRows = []
        #keep track when the description block starts.
        descriptionLoop = False
        for row in unCleanedRows:
            #if in description block make descriptionLoop true.
            if descriptionLoop:
                #Edge-case when then file does not have either Homepage: or Original-Maintainer so we have to append the Package: <data> row to the cleanedRows
                # and turn off the descriptionLoop
                if "Package:" in str(row):
                    cleanedRows.append(str(row))
                    descriptionLoop = False
                    continue
                #Description block ends we run into these two.
                if "Homepage:" in str(row) or "Original-Maintainer:" in str(row):
                    descriptionLoop = False
                    continue
                cleanedRows.append(str(row))
            #This row marks the beginning of description block.
            if "Description:" in str(row):
                cleanedRows.append(str(row))
                descriptionLoop = True
            #Append Package and Depends rows to the cleanedRows but not Pre-Depends
            if "Package:" in str(row) or "Depends:" in str(row) and not "Pre-Depends:" in str(row):
                cleanedRows.append(str(row))

        return cleanedRows

    def makeTuplesFromCleanedRows(self, cleanedRows):
        # Gets the cleaned list as input and makes 2 or 3 tuples from the packages.
        # 2 tuples are of format: PackageName, PackageDescription
        # 3 tuples are of format: PackageName, PackageDependencies, Dependants
        tuples = []
        while (len(cleanedRows) > 0):
            if "Package:" in cleanedRows[0]:
                descriptionString = ""
                tempList = []
                #pop the row with Package: as first item of list.
                tempList.append(cleanedRows.pop(0))
                while (True):
                    if len(cleanedRows) <= 0:
                        break
                    #Beginning of Description block.
                    if "Description:" in cleanedRows[0]:
                        #Since its a list of String strip away [' and '] and append it into the descriptionString
                        descriptionString += (cleanedRows.pop(0)[2:-2])
                        #add html newline for the future html rendering.
                        descriptionString += "<br>"
                        # add all rows belonging to the current package description to the descriptionString
                        while (True):
                            #Description rows end when the next package starts.
                            if len(cleanedRows) <= 1 or "Package:" in cleanedRows[0]:
                                #append description as the second item of the list.
                                tempList.append(descriptionString)
                                break
                            # Since its a list of String strip away [' and '] and random ' then append it into the descriptionString
                            descriptionString += (cleanedRows.pop(0)[2:-2].strip("'"))
                            descriptionString += "<br>"
                    #When a new package starts we make a tuple from the list of 2 or 3 items and append it to the the list of tuples.
                    if "Package:" in cleanedRows[0]:
                        tuples.append(tuple(tempList))
                        break
                    # If its not the package then its the Depends row that get appended as the third list item.
                    else:
                        tempList.append(cleanedRows.pop(0))
        return tuples



    def generateDependants(self):
        for package in self.packages:
            package.findDependants(self.packages)

    def getPackages(self):
        return self.packages


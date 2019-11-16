import re
import sys
sys.path.insert(0, '')

class Package:
    def __init__(self, packageInfo):
        self.cleanAndUnpackTuples(packageInfo)

        self.packageName
        self.packageDescription
        self.packageDependancies
        self.packagesDependant = []

        #clean dependencies if we have them.
        if self.packageDependancies:
            self.stripDependencies()

    def cleanAndUnpackTuples(self, packageData):
        # packageInfo should always be 2 or 3 item tuple so there are two possible choices.
        if len(packageData) == 2:
            #Clean the string to only have packagename
            self.packageName = packageData[0].split(": ")[1].split("'")[0]
            #Clean ' and random double spaces.
            self.packageDescription = packageData[1].replace("'", "").replace("  ", " ")
            #2 item tuples have 0 dependencies.
            self.packageDependancies = None
        elif len(packageData) == 3:
            # Clean the string to only have packagename
            self.packageName = packageData[0].split(": ")[1].split("'")[0]
            #Remove the Depends: part from the string.
            self.packageDependancies = packageData[1].split(": ")[1]
            # Clean ' and random double spaces.
            self.packageDescription = packageData[2].replace("'", "").replace("  ", " ")
        else:
            raise Exception('Parsing failed somewhere.')

    def stripDependencies(self):
            #Split into a list of dependencies.
            self.packageDependancies = self.packageDependancies.split(",")
            for index in range(len(self.packageDependancies)):
                # remove version numbers if they exist.
                if "(" in self.packageDependancies[index]:
                    self.packageDependancies[index] = re.sub(r'\([^)]*\)', '', self.packageDependancies[index])
                #Clean dependencies in the list.
                self.packageDependancies[index] = self.packageDependancies[index].replace("'", "").replace("]", "").strip()


    def getDependancies(self):
        return self.packageDependancies

    def findDependants(self, allPackages):
        #Loops through all the packages and looks if some package is dependant from this one.
        for package in allPackages:
            if package.getDependancies():
                for dependency in package.getDependancies():
                    if self.packageName in dependency and package.packageName not in self.packagesDependant:
                        self.packagesDependant.append(package.packageName)

    def getDependants(self):
        return self.packagesDependant

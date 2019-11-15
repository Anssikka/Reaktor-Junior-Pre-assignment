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
        if self.packageDependancies:
            self.packageDependancies = self.packageDependancies.split(",")
            for index in range(len(self.packageDependancies)):
                if "(" in self.packageDependancies[index]:
                    # remove version numbers.
                    self.packageDependancies[index] = re.sub(r'\([^)]*\)', '', self.packageDependancies[index])
                self.packageDependancies[index] = self.packageDependancies[index].replace("'", "").replace("]", "").strip()

    def print(self):
        print("Packagename: ", self.packageName, "PackageDescription: ", self.packageDescription, "packageDependancies: ", self.packageDependancies, "PackagesDependant: ", self.packagesDependant)

    def getDependancies(self):
        return self.packageDependancies

    def findDependants(self, allPackages):
        for package in allPackages:
            if package.getDependancies():
                for singleDependancy in package.getDependancies():
                    # Check if the dependency has alternatives
                    if "|" in singleDependancy:
                        # Get the first one since that has an url in the directory
                        dependencyWithAlternatives = singleDependancy.split("|")[0].strip()
                        if self.packageName == dependencyWithAlternatives:
                            self.packagesDependant.append(package.packageName)
                    elif self.packageName == singleDependancy:
                        self.packagesDependant.append(package.packageName)

    def getDependants(self):
        return self.packagesDependant

    def getHref(self):
        return "<li><a href = './Packages/{}.html'>{}</a></li> \n".format(self.packageName, self.packageName)

    def getPackageNameHeader(self):
        return "<h1>{}</h1>".format(self.packageName)

    def getDescriptionHeader(self):
        return "<p>{}</p>".format(self.packageDescription)

    def getDependanciesHrefs(self):
        str = ""
        if self.packageDependancies:
            for dep in self.packageDependancies:
                # If there are alternatives make the first one a link, alternatives are appended after it without links.
                if "|" in dep:
                    dep = dep.split("|")
                    dep[0] = dep[0].strip()
                    str += "<li><a href = './{}.html'>{}</a> | {}</li> \n".format(dep[0], dep[0], dep[1])
                else:
                    str += "<li><a href = './{}.html'>{}</a></li> \n".format(dep, dep)
        return str

    def getDependantHrefs(self):
        str = ""
        if self.packagesDependant:
            for dep in self.packagesDependant:
                str += "<li><a href = './{}.html'>{}</a></li> \n".format(dep, dep)
        return str
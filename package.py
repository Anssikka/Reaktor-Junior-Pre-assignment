class Package:
    def __init__(self, packageInfo):

        #packageInfo is always on same format so there are two possible choices.
        if len(packageInfo) == 2:
            self.packageName = packageInfo[0].split(": ")[1].split("'")[0]
            self.packageDescription = packageInfo[1].split(": ")[1].split("'")[0]
            self.packageDependancies = None
        else:
            self.packageName = packageInfo[0].split(": ")[1].split("'")[0]
            self.packageDependancies = packageInfo[1].split(": ")[1]
            ##TODO lines with |


            self.packageDescription = packageInfo[2].split(": ")[1].split("'")[0]
        self.packagesDependant = []

        #Make dependancies more readable and strip ' ] and whitespace.
        if self.packageDependancies:
            self.packageDependancies = self.packageDependancies.split(",")
            for index in range(len(self.packageDependancies)):
                if "(" in self.packageDependancies[index]:
                    self.packageDependancies[index] = self.packageDependancies[index].split("(")[0]
                self.packageDependancies[index] = self.packageDependancies[index].replace("'", "").replace(" ", "").replace("]","")

    def print(self):
        print("Packagename: ",self.packageName,"PackageDescription: ", self.packageDescription, "packageDependancies: ", self.packageDependancies, "PackagesDependant: ", self.packagesDependant)

    def getDependancies(self):
        return self.packageDependancies

    #Use strict equality to find all the packages that are dependant on this one from a list of packages.
    def findDependants(self, allPackages):
        for package in allPackages:
            if package.getDependancies() and self.packageName in package.getDependancies():
                self.packagesDependant.append(package.packageName)

    def getDependants(self):
        return self.packagesDependant

    def getHref(self):
        return "<li><a href = ""./Packages/{}.html>""{}</a></li>".format(self.packageName, self.packageName)

    def getPackageNameHeader(self):
        return "<h1>{}</h1>".format(self.packageName)

    def getDescriptionHeader(self):
        return "<p>{}</p>".format(self.packageDescription)

    def getDependanciesHrefs(self):
        str = ""
        if self.packageDependancies:
            for dep in self.packageDependancies:
                str += "<li><a href = ""./{}.html>""{}</a></li> \n".format(dep, dep)
        return str

    def getDependantHrefs(self):
        str = ""
        if self.packagesDependant:
            for dep in self.packagesDependant:
                str += "<li><a href = ""./{}.html>""{}</a></li> \n".format(dep, dep)
        return str
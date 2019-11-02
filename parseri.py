from csv import reader
import os

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
        print("packagename: ",self.packageName,"packageDescription: ", self.packageDescription, "packageDependancies: ", self.packageDependancies, "PackagesDependant: ", self.packagesDependant)

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


class Util:
    def __init__(self, path):
        file = open(path, encoding="utf8")
        readPackages = reader(file)
        statusRows = list(readPackages)
        #Get only required rows.
        cleanedRows = []
        ###
        filterWords = ["Package:", "Description:", "Depends:"]
        illegalWord = "Pre-Depends:"
        ###
        #print('Statusrows: ', len(statusRows))
        for row in statusRows:
            if filterWords[0] in str(row) or filterWords[1] in str(row) or filterWords[2] in str(row) and not illegalWord in str(row):
                cleanedRows.append(str(row))


        #print('Cleanedrows: ', len(cleanedRows))
        #Make tuples out of the packages for easier processing.
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

        #print('Tuples: ', len(tuples))
        #Turn Tuples into Package objects.
        self.packages = [Package(tupleVar) for tupleVar in tuples]

        #print('Packages:', len(self.packages))

    def generateDependants(self):
        for package in self.packages:
            package.getDependants()

    def generateIndex(self):
        f = open("index.html", "w+")
        f.write('<ul>')
        for package in self.packages:
            f.write(package.getHref())
        f.write('</ul>')
        f.close()

    def generatePackagesDir(self):
        for package in self.packages:
            dir = "./Packages/{}.html".format(package.packageName)
            f = open(dir, "w+")
            html = """
            <div>
               <H1>{}</H1>
               <h3>{}</h3>
               <h3>Dependencies:</h3>
               <ul>
                {}
               </ul>
               <h3>Dependants:</h3>
               <ul>
                {}
               </ul>
           </div>
           <div><a href="../index.html">Back to index</a></div>

            """.format(package.packageName, package.packageDescription, package.getDependanciesHrefs(),
                       package.getDependantHrefs())
            f.write(html)
        f.close()

if not os.path.isdir("./Packages"):
    os.mkdir("./Packages")


utility = Util('status.real')
utility.generateIndex()
utility.generateDependants()
utility.generatePackagesDir()


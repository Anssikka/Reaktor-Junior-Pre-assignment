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


file = open('status.real', encoding="utf8")
read_file = reader(file)
statusPackages = list(read_file)

#Siivotaan vain tarvittavat statusPackages.

siivotut = []
for row in statusPackages:
    if "Package:" in str(row) or "Description:" in str(row) or "Depends:" in str(row) and not "Pre-Depends:" in str(row):
        siivotut.append(str(row))

# Tehdään packageista tuplet

tuplet = []
while len(siivotut) > 0:
    if "Package:" in siivotut[0]:
        tempList = []
        tempList.append(siivotut.pop(0))
        while (True):
            if len(siivotut) <= 0:
                break
            if "Package:" in siivotut[0]:
                tuplet.append(tuple(tempList))
                break
            else:
                tempList.append(siivotut.pop(0))


#tehdään packageClassit
paketit = []
for package in tuplet:
    paketit.append(Package(package))

#haetaan dependantit
for p in paketit:
    p.findDependants(paketit)


paketit
for pakkake in paketit:
    if pakkake.getDependants():
        if len(pakkake.getDependants()) > 0:
            pakkake.print()


f = open("index.html", "w+")
f.write('<ul>')

#Generoidaan indeksi
for package in paketit:
    f.write(package.getHref())

f.write('</ul>')
f.close()



for package in paketit:
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

    """.format(package.packageName, package.packageDescription, package.getDependanciesHrefs(), package.getDependantHrefs())
    f.write(html)

f.close()

#Generoidaan hakemistot
# for row in tuplet:
#     packageName = row[0]
#     packageName = packageName.split(": ")
#     nimi = packageName[1].split("'")[0]
#
#     dir = "./Packages/{}.html".format(nimi)
#
#
#     f = open(dir, "w+")
#     html = """
#           <div>
#               <H1>{}</H1>
#               <h3>{}</h3>
#               <h3></h3>
#               <ul>
#                 <li>linkki</li>
#                 <li>linkki</li>
#               </ul>
#           </div>
#
#          """.format(nimi, row[1])
#     f.write(html)
#     f.close()
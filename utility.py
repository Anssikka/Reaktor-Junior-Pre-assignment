from csv import reader
from package import Package

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
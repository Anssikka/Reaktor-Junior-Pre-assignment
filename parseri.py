from csv import reader
import os


class Package:
    def __init__(self, packageInfo):
        if len(packageInfo) == 2:
            self.packageName = packageInfo[0].split(": ")[1].split("'")[0]
            self.packageDescription = packageInfo[1].split(": ")[1].split("'")[0]
            self.packageDepends = None
        else:
            self.packageName = packageInfo[0].split(": ")[1].split("'")[0]
            self.packageDepends = packageInfo[1].split(": ")[1]
            self.packageDescription = packageInfo[2].split(": ")[1].split("'")[0]

        #format dependencies to more readable format
        if self.packageDepends:
            self.packageDepends = self.packageDepends.split(",")
            for index in range(len(self.packageDepends)):
                if "(" in self.packageDepends[index]:
                    self.packageDepends[index] = self.packageDepends[index].split("(")[0]
                self.packageDepends[index] = self.packageDepends[index].replace("'", "").replace(" ", "").replace("]","")


    def print(self):
        print("packagename: ",self.packageName," packageDescription: ", self.packageDescription, "PackageDepends: ", self.packageDepends)

file = open('status.txt', encoding="utf8")
read_file = reader(file)
rivit = list(read_file)

def explore_data(dataset, start, end):
    for row in dataset:
        print(row)

#Siivotaan vain tarvittavat rivit.

siivotut = []
for row in rivit:
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

#for row in tuplet:
    #if len(row) == 2:
        #print(row)


paketit = []
for package in tuplet:
    paketit.append(Package(package))

paketit = paketit[3:12]
for pakkake in paketit:
    pakkake.print()



#f = open("index.html", "w+")
#f.write('<ul>')

#tuplet = tuplet[:15]
# Generoidaan indeksi
# for row in tuplet:
#     packageName = row[0]
#     packageName = packageName.split(": ")
#     nimi = packageName[1].split("'")[0]
#     str = "<a href = ""./Packages/{}.html>""{}</a>".format(nimi, nimi)
#     if len(row) == 3:
#         print(row)
#
#     f.write("<li> {} </li> \n".format(str))
#
# f.write('</ul>')
# f.close()

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
from csv import reader
import os

file = open('status.txt', encoding="utf8")
read_file = reader(file)
rivit = list(read_file)

def explore_data(dataset, start, end):
    for row in dataset:
        print(row)

#Siivotaan vain tarvittavat rivit.

siivotut = []
for row in rivit:
    if "Package:" in str(row) or "Description:" in str(row) or "Depends:" in str(row):
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

f = open("index.html", "w+")

f.write('<ul>')

# Generoidaan indeksi
for row in tuplet:
    packageName = row[0]
    packageName = packageName.split(": ")
    nimi = packageName[1].split("'")[0]
    str = "<a href = ""/Packages/{}>""{}</a>".format(nimi, nimi)
    f.write("<li> {} </li> \n".format(str))

f.write('</ul>')
f.close()

#Generoidaan hakemistot
for row in tuplet:
    packageName = row[0]
    packageName = packageName.split(": ")
    nimi = packageName[1].split("'")[0]

    dir = "./Packages/{}.html".format(nimi)


    f = open(dir, "w+")
    html = """
          <div>
              <H1>{}</H1>
              <h3>{}</h3>
              <h3></h3>
              <ul>
                <li>linkki</li>
                <li>linkki</li>
              </ul>
          </div>
    
         """.format(nimi, row[1])
    f.write(html)
    f.close()
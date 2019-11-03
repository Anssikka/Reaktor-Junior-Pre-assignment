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
            package.findDependants(self.packages)


    def generateIndex(self):
        self.packages.sort(key=lambda x: x.packageName)
        f = open("./build/index.html", "w+")
        html = """<!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="UTF-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1.0">
                  <meta http-equiv="X-UA-Compatible" content="ie=edge">
                  <link rel="stylesheet" href="styles.css">
                  <title>Document</title>
                </head>
                <body>
                 <ul>"""
        f.write(html)
        for package in self.packages:
            f.write(package.getHref())
        f.write('</ul></body></html>')
        f.close()

    def generateIndexCss(self):
        f = open("./build/styles.css", "w+")
        css = """
            body {
              background-color: #100e17;
              font-family: 'Open Sans', sans-serif;
            }
            
            ul {
              color: white;
              list-style-type: square;
            }
            
            a {
              color:white;
              font-size: 125%;
            }
        """
        f.write(css)
        f.close()


    def generatePackagesDir(self):
        for package in self.packages:
            dir = "./build/Packages/{}.html".format(package.packageName)
            f = open(dir, "w+")
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <link rel="stylesheet" href="styles.css">
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <meta http-equiv="X-UA-Compatible" content="ie=edge">
              <title>Document</title>
            </head>
            <body>
            <div class="container">
              <div class="card">
                <h2 class="title">{}</h2>
                <div class="bar">
                  <div class="description">
                    <h3>{}</h3>
                  </div>
                  <div class=linkToIndex><a href="../index.html">Back to index</a></div>
                  <div class="emptybar"></div>
                  <div>
                    <h3>Dependencies:</h3>
                    <ul class= dlist>
                      {}
                    </ul>
                    <h3>Dependants:</h3>
                    <ul>
                      {}       
                    </ul>
                  
                  </div>
                </div>
            </body>
            </html>
            """.format(package.packageName, package.packageDescription, package.getDependanciesHrefs(),
                       package.getDependantHrefs())
            f.write(html)
        f.close()

    def generatePackagesCss(self):
        f = open("./build/Packages/styles.css", "w+")
        css = """
            body {
              background-color: #100e17;
              font-family: 'Open Sans', sans-serif;
            }
            
            .container {
              position: relative;
              height: 100%;
              width: 600px;
              top: 60px;
              left: calc(50%);
              display: flex;
            }
            
            .card {
              display: flex;
              height: 1200px;
              width: 220px;
              background-color: #17141d;
              border-radius: 10px;
              box-shadow: -1rem 0 3rem #000;
              transition: 0.4s ease-out;
              position: relative;
              left: 0px;
            }
            
            .title {
              color: white;
              font-weight: 1500%;
              position: absolute;
              left: 20px;
              top: 15px;
            }
            
            .description {
              color: white;
              font-weight: 150;
              padding-top: 35px;
            }
            
            h3 {
              color: white;
              font-weight: 150;
            }
            
            .bar {
              position: absolute;
              top: 75px;
              left: 20px;
              height: 5px;
              width: 150px;
            }
            
            .emptybar {
              background-color: #2e3033;
              width: 100%;
              height: 100%;
            }
            
            li {
              color: white;
            }
            
            .linkToIndex {
              position: relative;
              bottom: 5px;
              left: 30px;
            }
            
            a {
              color: white;
              text-align: center;
            }
            
            .dlist {
              list-style-type: square;
            }
        """
        f.write(css)
        f.close()

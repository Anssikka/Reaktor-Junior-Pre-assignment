from csv import reader
from package import Package

class Util:
    def __init__(self, path):
        file = open(path, encoding="utf8")
        readPackages = reader(file)
        statusRows = list(readPackages)
        #Get only required rows.
        filterWords = ["Package:", "Description:", "Depends:"]
        illegalWord = "Pre-Depends:"
        cleanedRows = []
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

        #Turn Tuples into Package objects.
        self.packages = [Package(tupleVar) for tupleVar in tuples]

        #print('Packages:', len(self.packages))

    def generateDependants(self):
        for package in self.packages:
            package.findDependants(self.packages)

    def getPackages(self):
        return self.packages

    def generateIndex(self):
        self.packages.sort(key=lambda x: x.packageName)
        f = open("./build/index.html", "w+")
        html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="style.css" />
    <title>Package List</title>
  </head>
  <body>
    <main class="container horizontal-center">
      <h1 class="text-center">List of Packages</h1>
      <article>List of all packages found on the system</article>
      <section class="box">
      <ul>"""
        f.write(html)
        for package in self.packages:
            f.write(package.getHref())
        f.write('</ul></section></body></html>')
        f.close()

    def generateCss(self):
        f = open("./build/style.css", "w+")
        css = """
@import url('https://fonts.googleapis.com/css?family=IBM+Plex+Mono:300+400,700&display=swap');

/* For better accessibility */
*:focus:not(:hover) {
  background: #121212;
  color: #fafafa;
  padding: 0.5rem;
}

*:focus:visited {
  background: rgb(231, 96, 18);
  color: #fafafa;
  padding: 0.5rem;
}

body {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 16px;
  display: flex;
  background-image: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%);
  color: #121212;
}

.text-center {
  text-align: center;
}

h1 {
  font-size: 2rem;
  font-weight: 300;
}

h2 {
  font-size: 1.7rem;
  font-weight: 700;
}

h3 {
  font-size: 1.4rem;
  font-weight: 700;
}

.container {
  max-width: 80%;
  display: flex;
  flex-direction: column;
  margin: auto;
}

article {
  font-size: 1.2rem;
}

li,
a {
  list-style-type: none;
  font-size: 1.2rem;
  line-height: 2rem;
  color: rgb(43, 42, 39);
}

a:visited {
  color: rgb(231, 96, 18)
}

a:hover {
  background: rgb(231, 96, 18);
  color: white;
  padding: 0.2rem;
}

section {
  padding: 0.5rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.box {
  background-color: white;
  border-radius: 0.8rem;
  box-shadow: 10px 10px 10px -4px rgba(0, 0, 0, 0.20);
  padding: 1rem;
}

section>h3 {
  margin-top: 0;
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
  <link rel="stylesheet" href="../style.css">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title> {} | Package List</title>
</head>

<body>
  <main class="container horizontal-center">
    <h1 class="text-center">List of Packages</h1>
    <h2 class="text-center">{}</h2>
    <article class="text-center">{}
      <br><a href="../index.html">Back to index</a>
    </article>
    <section class="box">
      <h3 class="text-center">Dependencies</h3>
      <ul>
        {}
      </ul>
    </section>
    <section class="box">
      <h3 class="text-center">Dependants</h3>
      <ul>
        {}
      </ul>
    </section>
  </main>
</body>
</html>
            """.format(package.packageName, package.packageName, package.packageDescription, package.getDependanciesHrefs(),
                       package.getDependantHrefs())
            f.write(html)
        f.close()

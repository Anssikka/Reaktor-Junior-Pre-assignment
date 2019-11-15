import os
from Modules.parser import Parser
from Modules.htmlgenerator import HtmlGenerator

if not os.path.isdir("./build/"):
    os.mkdir("./build")
if not os.path.isdir("./build/Packages/"):
    os.mkdir('./build/Packages')

parser = Parser('status.real')
htmlGenerator = HtmlGenerator(parser.getPackages())
htmlGenerator.generateIndex()
htmlGenerator.generateCss()
htmlGenerator.generatePackagesDir()

for package in parser.getPackages():
    if package.getDependancies():
        for dep in package.getDependancies():
            if "|" in dep:
                print(package.packageName)

print("Succesfully generated files!")
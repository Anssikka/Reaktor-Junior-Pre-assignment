import os
from Modules.parser import Parser
from Modules.htmlgenerator import HtmlGenerator
from csv import reader

if not os.path.isdir("./build/"):
    os.mkdir("./build")
if not os.path.isdir("./build/Packages/"):
    os.mkdir('./build/Packages')

parser = Parser('status.real')
htmlGenerator = HtmlGenerator(parser.getPackages())
htmlGenerator.generateIndex()
htmlGenerator.generateCss()
htmlGenerator.generatePackagesDir()

print("Succesfully generated files!")

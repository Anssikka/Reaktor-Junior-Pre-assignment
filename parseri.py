import os
from Modules.utility import Utiliti

if not os.path.isdir("./build/"):
    os.mkdir("./build")
if not os.path.isdir("./build/Packages/"):
    os.mkdir('./build/Packages')

utility = Utiliti('status.real')
utility.generateIndex()
utility.generateCss()
utility.generateDependants()
utility.generatePackagesDir()


print("Succesfully generated files!")
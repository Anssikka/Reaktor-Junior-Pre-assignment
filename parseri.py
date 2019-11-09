import os
from utility import Util

if not os.path.isdir("./build/"):
    os.mkdir("./build")
if not os.path.isdir("./build/Packages/"):
    os.mkdir('./build/Packages')

utility = Util('status.real')
utility.generateIndex()
utility.generateCss()
utility.generateDependants()
utility.generatePackagesDir()




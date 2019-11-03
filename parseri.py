import os
from utility import Util

if not os.path.isdir("./build/"):
    os.mkdir("./build")
os.mkdir('./build/Packages')
if not os.path.isdir("./build/Packages/"):
    os.mkdir('./build/Packages')


utility = Util('status.real')
utility.generateIndex()
utility.generateIndexCss()
utility.generateDependants()
utility.generatePackagesDir()
utility.generatePackagesCss()


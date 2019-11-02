import os
from utility import Util

if not os.path.isdir("./Packages"):
    os.mkdir("./Packages")


utility = Util('status.real')
utility.generateIndex()
utility.generateDependants()
utility.generatePackagesDir()


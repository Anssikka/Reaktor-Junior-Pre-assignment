import sys
sys.path.insert(0, '')
from Modules.parser import Parser
from Modules.package import Package
import pytest

parser = Parser('./Tests/statustest.real')

class TestParser():
    def test_rightAmountOfPackages(self):
        assert len(parser.getPackages()) == 382

    def test_rightAmountOfTotalDependencies(self):
        totalDependencies = 0
        for package in parser.getPackages():
            if package.getDependancies():
                totalDependencies += len(package.getDependancies())
        assert totalDependencies == 1055

    def test_rightAmountofTotalDependants(self):
        totalDependants = 0
        for package in parser.getPackages():
            if package.getDependants():
                totalDependants += len(package.getDependants())
        assert totalDependants == 494


package = Package(("['Package: bsh-gcj']", "['Depends: bsh (= 2.0b4-12build1)', ' libgcj-common (>> 1:4.1.1-13)', ' libc6 (>= 2.2.5)', ' libgcc1 (>= 1:4.1.1)', ' libgcj-bc (>= 4.4.5-1~)']", "['Description: Java scripting environment (BeanShell) Version 2 (native code)']"))
secondPackage = Package
for p in parser.getPackages():
    if "adduser" in p.packageName:
        secondPackage = p

class TestPackageTests():
    def test_packageNameIsCorrect(self):
        assert package.packageName == "bsh-gcj"

    def test_packageDescriptionIsCorrect(self):
        assert str(package.packageDescription) == "Java scripting environment (BeanShell) Version 2 (native code)"

    def RightAmountOfDependencies(self):
        assert len(package.getDependancies()) == 5

    def test_stripDependenciesIsCorrect(self):
        assert str(package.getDependancies()) == "['bsh', 'libgcj-common', 'libc6', 'libgcc1', 'libgcj-bc']"

    def test_amountOfDependantsCorrect(self):
        assert len(secondPackage.getDependants()) == 3

    def test_dependantsAreCorrect(self):
        assert (str(secondPackage.getDependants())) == "['wpasupplicant', 'tomcat6', 'dbus']"
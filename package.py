class Package:
    def __init__(self, packageInfo):
        if len(packageInfo) == 2:
            self.packageName = packageInfo[0].split(": ")[1].split("'")[0]
            self.packageDescription = packageInfo[1].split(": ")[1].split("'")[0]
        else:
            self.packageName = packageInfo[0].split(": ")[1].split("'")[0]
            self.packageDepends = packageInfo[1].split(": ")[1]
            self.packageDescription = packageInfo[2].split(": ")[1].split("'")[0]

        #format dependencies to more readable format
        self.packageDepends = self.packageDepends.split(",")
        for index in range(len(self.packageDepends)):
            if "(" in self.packageDepends[index]:
                self.packageDepends[index].split("(")[0]
            self.packageDepends[index].replace("'", "").replace(" ", "")


    def print(self):
        print("packagename: ",self.packageName," packageDescription: ", self.packageDescription, "PackageDepends: ", self.packageDepends)
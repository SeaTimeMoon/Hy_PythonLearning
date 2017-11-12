class People:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error name length, the length must be above 5 chars")


xiaoming = People("xiaoming")
print(xiaoming.getName())
xiaoming.setName("huahua")
print(xiaoming.getName())
xiaoming.setName("haha")
print(xiaoming.getName())
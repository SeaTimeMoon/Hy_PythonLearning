class Cat():
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color

    def run(self):
        print("%s is running"%self.name)

class Bosi(Cat):
    def setNewName(self, newName):
        self.name = newName
    def eat(self):
        print("%s is eating"%self.name)

class Animal():
    def __init__(self, name='animal', color='white'):
        self.__name = name #私有属性不能被对象直接调用，不能被子类继承
        self.color = color

    #私有方法不能被对象直接访问，不能被子类继承
    def __test(self):
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)

class Dog(Animal):
    def dogTest1(self):
        print(self.color)

    def dogTest2(self):
        self.test()


bs = Bosi("India Cat")
print("bs's name is %s"%bs.name)
print("bs's color is %s"%bs.color)
bs.eat()
bs.setNewName("Bosi Cat")
print("bs's name is %s"%bs.name)
bs.run()

print("-"*20) #seperate line
print("-"*20)

A = Animal()
print(A.color)
A.test()

print("-"*20) #seperate line

D = Dog(name='LittlePuppy', color='yellow')
D.dogTest1()
D.dogTest2()

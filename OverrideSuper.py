class Cat():
    def __init__(self,name):
        self.name = name
        self.color = 'yellow'

    def __str__(self):
        return "A cat's name is " + self.name + " and its color is " + self.color

    def sayHello(self):
        print("Hello, I am a cat")

class Bosi(Cat):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return "A Bosi cat's name is " + self.name + " and its color is " + self.color

    def sayHello(self):
        print("Hello, I am a cute Bosi Cat")

Kiky = Cat("Kiky")
print(Kiky)
Kiky.sayHello()

Bob = Bosi("Bob")
print(Bob)
Bob.sayHello()


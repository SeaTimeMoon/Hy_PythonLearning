
class Animal():
    def __init__(self, name):
        print("__init__ is called")
        self.__name = name

    def __del__(self):
        print("__del__ is called")
        print("%s objected is going to be deleted.."%self.__name)


dog = Animal("Puppy")
del dog

cat = Animal("BosiCat")
cat2 = cat
cat3 = cat

print("Prepared for deletion:")
del cat
print("Prepared for deletion:")
del cat2
print("Prepared for deletion:")
del cat3

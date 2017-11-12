class People():
    #类属性
    country = 'China'
    address = 'Shanghai'
    def __init__(self):
        self.name = 'carl'
        self.age = 20
     #类方法，用classmethod来修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country, address):
        cls.country = country
        cls.address = address

print(People.country)
print(People.address)
print('-'*20)
p = People()
print(p.country)
print(p.address)
print('-'*20)
p.country = 'Japan' #实例属性会屏蔽掉同名的类属性
p.address = 'Tokyo'
print(p.country)
print(p.address)
print('-'*20)
del p.country
del p.address
print(p.country)
print(p.address)
print('-'*20)
p.setCountry(country='Japan', address='Tokyo')
print(p.country)
print(p.address)
print('-'*20)
print(People.country)
print(People.address)

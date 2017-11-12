#子弹类
class Bullet:
    def __init__(self, damage):
        self.damage = damage
    def damageEnemy(self, enemy):
        enemy.loseBlood(self.damage)

#弹夹类
class Magazine:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bulletList = []

    def __str__(self):
        return "The Magazine fills with " + str(len(self.bulletList)) +\
               " bullets" + " with capacity of " + str(self.capacity)

    def saveBullet(self, bullet):
        if len(self.bulletList) < self.capacity:
            self.bulletList.append(bullet)

    def popBullet(self):
        #判断当前弹夹中是否还有子弹
        if len(self.bulletList) > 0:
            #获取最后压入到弹夹中的子弹
            bullet = self.bulletList[-1]
            self.bulletList.pop()
            return bullet
        else:
            return None

#枪类
class Gun:
    def __init__(self):
        self.magazine = None

    def __str__(self):
        if self.magazine:
            return "The Gun loads a magazine"
        else:
            return "The Gun is loaded without magazines"

    def connectMagazine(self, magazine):
        if not self.magazine:
            self.magazine = magazine

    def fire(self, enemy):
        bullet = self.magazine.popBullet()
        if bullet:
            bullet.damageEnemy(enemy)
        else:
            print("Run out of bullets")

#人类
class Person:
    def __init__(self, name):
        self.name = name
        self.blood = 100
        self.gun = None

    def __str__(self):
        return self.name + " remain blood:" + str(self.blood)

    def loadingBullet(self, magazine, bullet):
        magazine.saveBullet(bullet)

    def connectMagazine(self, gun, magazine):
        gun.connectMagazine(magazine)

    def holdGun(self, gun):
        self.gun = gun

    def fire(self, enemy):
        self.gun.fire(enemy)

    def loseBlood(self, damage):
        self.blood -= damage



#创建一个人对象
MrWang = Person("laowang")

#创建一个弹夹
magazine = Magazine(20)
print(magazine)

#循环的方式创建一颗子弹，然后把子弹压入到弹夹中
i=0
while i<5:
    bullet = Bullet(5)
    MrWang.loadingBullet(magazine, bullet)
    i+=1
print(magazine)

#创建一个枪对象
gun = Gun()
print(gun)
#连接弹夹
MrWang.connectMagazine(gun,magazine)
print(gun)

#持枪
MrWang.holdGun(gun)

#创建一个敌人
enemy = Person("enemy")
print(enemy)

#开枪杀敌人
MrWang.fire(enemy)
print(enemy)
print(magazine)

MrWang.fire(enemy)
print(enemy)
print(magazine)



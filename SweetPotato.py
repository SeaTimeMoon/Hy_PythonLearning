
class SweetPotato:
    """
    这是烤地瓜类
    """

    #定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    #定制print时的显示内容
    def __str__(self):
        msg = self.cookedString + "地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("

            for temp in self.condiments:
                msg = msg + temp +", "
            msg = msg.strip(", ")

            msg = msg + ")"
        return msg

    #烤地瓜方法
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel >8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    #添加配料
    def addCondiments(self, condiments):
        self.condiments.append(condiments)

#用来进行测试
mySweetPotato = SweetPotato()
print("------有了一个地瓜，还没有烤-----")
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)
print("------接下来要进行烤地瓜了-----")
print("------地瓜经烤了4分钟-----")
mySweetPotato.cook(4)
print(mySweetPotato)
print("------地瓜又经烤了3分钟-----")
mySweetPotato.cook(3)
print(mySweetPotato)
print("------接下来要添加配料-番茄酱------")
mySweetPotato.addCondiments("番茄酱")
print(mySweetPotato)
print("------地瓜又经烤了5分钟-----")
mySweetPotato.cook(5)
print(mySweetPotato)
print("------接下来要添加配料-芥末酱------")
mySweetPotato.addCondiments("芥末酱")
print(mySweetPotato)
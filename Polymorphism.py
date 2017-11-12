#多态示例

class F1():
    def show(self):
        print('F1 show')

class S1(F1):
    def show(self):
        print('S1 show')

class S2(F1):
    def show(self):
        print('S2 show')

def Func(obj):
    obj.show()

f1 = F1()
Func(f1)

s1 = S1()
Func(s1)

s2 = S2()
Func(s2)
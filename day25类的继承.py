class Dad:
    '这个是爸爸类'
    money=10
    def __init__(self,name):
        print('爸爸')
        self.name=name

    def hit_son(self):
        print('%s 正在打儿子'%self.name)

class Son(Dad):
    money = 1000000
    def __init__(self,name,age):
        self.name = name
        self.age = age
    pass

# print(Son.money)
# #Son.hit_son()
# print(Son.__dict__)
# print(Dad.__dict__ )
S1=Son('alex',18)
print(S1.money)#属性先找自己 再找父类
S1.hit_son()
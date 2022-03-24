# dic = {'k1':123,456:123,'999':123}
# v = dic.pop("k1")
# print(v)
# print(dic)
#python 一切皆对象
class H2O:
    def __init__(self,name,Tem):
        self.name=name
        self.Tem=Tem

    def turn_ice(self):
        if self.Tem > 100:
            print('[%s]变成水蒸气'%self.name)
        elif self.Tem < 0:
            print('[%s]变成冰' % self.name)
        else:
            print('[%s]变成水' % self.name)
class Water(H2O):
    pass

class Ice(H2O):
    pass

class Steam(H2O):
    pass

w1=Water('水',50)
w2=Ice('冰',-1)
w3=Steam('水蒸气',120)

w1.turn_ice()
w2.turn_ice()
w3.turn_ice()

def func(cj):
    cj.turn_ice()

func(w1)
func(w2)
func(w3)

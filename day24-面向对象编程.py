
class Dog:
    dang='共产党'
    def yao_ren():
        print('一条疯狗在叫')
    def zhao_sheng(self):
        pass
print(Dog)
print(Dog.dang)
Dog.yao_ren()
print(Dog.__dict__['dang'])#类有个属性字典 本质就是在查属性字典
Dog.__dict__['yao_ren']()
print(Dog.__name__)
print(Dog.__base__)
print(Dog.__module__)
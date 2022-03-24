#判断object中是否有一个name字符串的方法或者属性
class BlackMedium:
    feture='ugly'
    def __init__(self,name,addr,):
        self.name=name
        self.addr=addr

    def sell_hourse(self):
        print('[%s]  正在卖房子'% self.name)
    def rent_hourse(self):
        print('[%s]租房子' % self.name)

b1=BlackMedium('安家','天露园')
print(hasattr(b1,'name'))
print(hasattr(b1,'sell_hourse'))
print(getattr(b1,'name'))
print(getattr(b1,'sell_hourse'))#方法地址
setattr(b1,'aaa',123)
print(b1.__dict__)

#动态模块
# module_t=__import__('m1.t')
# print(module_t)
# module_t.t.test1()


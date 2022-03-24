#双下划线 attr 定义到我的类当中的

class Foo:
    x=1
    def __init__(self,y):
        self.y=y

    def __getattr__(self, item):#找不到对象属性不存在的时候出发运行 用处比较大
        print('执行__getattr__')
    # def __delattr__(self, item):#不会删除 如果不做操作
    #     print('执行__delattr__')
    def __setattr__(self, key, value):
        #elf.key=value#无线递归
        self.__dict__[key]=value
        print('执行__setattr__')
f1=Foo(10)
# print(f1.y)
# print(getattr(f1,'y'))
# f1.a
del f1.y
del f1.x
print(f1.x)



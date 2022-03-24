class Foo:
    def __init__(self,name):
        self.name=name

    def __setattr__(self, key, value):
        print(key,value)
        if type(value) is str:
            self.__dict__[key]=value
            print('设置成功')
        else:
            print('数据不是字符串')
    def __delattr__(self, item):
        print('不允许删除任何数据')
        self.__dict__.pop(item)
f1=Foo('alex')
f1.age=111
f1.x='aaa'
del f1.x
print(f1.x)
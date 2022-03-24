class Foo:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print('析构函数')

f1=Foo('cj')
del f1.name
print('-------------------------------')
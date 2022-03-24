class Foo:
    def __call__(self, *args, **kwargs):
        print('实例执行了')

f1=Foo()
f1()#Foo下的call方法

Foo()#object下的call方法
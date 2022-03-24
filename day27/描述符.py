#描述符本身应该定义成新式类 被代理的类也应该是新式类
#必须把描述符定义成这个类的类属性 不能定义到构造函数中
#要严格遵循该优先级 优先级高低分别是
# 1 类属性
# 2 数据描述符 有__set__ __get__
# 3 实例属性
# 4 非数据描述符  没有__set__
# 5 找不到的属性触发__getattr__
class Foo:

    def __set__(self, instance, value):
        print(' set方法====>')
        instance.__dict__['x']=value#b1.__dict__
    def __get__(self, instance, owner):
        print('get方法=====>')

    def __delete__(self, instance):
        print('del方法====>')

class Bar:
    x=Foo()

# print(Bar.x)
# Bar.x=1
# print(Bar.__dict__)

b1=Bar()
b1.x
Bar.x=111111111111111111111111
b1.x
print(b1.x)
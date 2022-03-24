
#__str__


class Foo:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def __str__(self):
    #     return  '自定制的对象的显示'

    def __repr__(self):#在解释器中触发
        # return  '名字是%s 年龄是%s' % (self.name,self.age)
        return '名字是%s 年龄是'
# f1=Foo()
# print(f1)#出发--str(f1)f1.__str__()
f1=Foo('egon',1)
print(f1)
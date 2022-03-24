class Foo:
    #__module__ __class__
    #__doc__不被继承
    #__slots__ = ['name';'age']#{'name':'None','age':'None'}
    __slots__ = 'name'

f1=Foo()
f1.name='cj'
print(f1.name)

print(f1.__slots__)
print(Foo.__slots__)
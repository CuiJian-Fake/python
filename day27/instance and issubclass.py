class Foo:
    pass

f1=Foo()
print(isinstance(f1,Foo))

class Bar(Foo):
    pass

f2=Bar()
print(issubclass(Bar,Foo))
# print(issubclass(f2,Foo))
print(type(f2))
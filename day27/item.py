class Foo:
    def __getitem__(self, item):
        print('getitem')

    def __setitem__(self, key, value):
        print('setitem')
        self.key=value

    def __delitem__(self, key):
        print('delitem')

f1=Foo()
print(f1.__dict__)
f1['name']='egon'
print(f1.__dict__) 
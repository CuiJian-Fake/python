class Foo:
    def __init__(self,y):
        self.y=y

    def __getattribute__(self, item):#
        print('==================>')
        # raise TabError('====>')
f1=Foo(1)
f1.y


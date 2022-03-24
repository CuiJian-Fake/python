class List(list):
    def show_middle(self):
        mid=int(len(self)//2)
        return self[mid]
    def append(self, object):
        if type(object) is str:
            super().append(object)
        else:
            print('不是需要的数据类型')

l1=List('helloworld')
print(l1,type(l1))
l2=list('hello word')
print(l2,type(l2))
print(l1.show_middle())
l1.append('abc')
print(l1)
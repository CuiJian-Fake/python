class Room:
    def __init__(self,name,long,height,width,owner):
        self.name=name
        self.long=long
        self.height=height
        self.width=width
        self.owner=owner
    @property#封装函数成数据属性
    def FF(self):
        print('%s住在%s 总面积%s'%(self.name,self.owner,int(self.width)*int(self.long)))
    @classmethod#只给类用来调用的
    def AA(cls):
        print(cls)
        print('ZZZZZZZZZZZZZZZ')
r1=Room('alex','10000','1000','100','wc',)
r1.FF
Room.AA()



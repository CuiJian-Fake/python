class People:
    __start='earth'
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def get_id(self):
        print('id 是 %s' % self.id)

    #接口函数
    def get_start(self):
        print(self.__start)
#单下划线 使用者和作者的约定 外部不调用
#双下划线 会给变量重新命名 _class__变量


import time
class Open:
    def __init__(self,filename,mode='r',encoding='UTF-8'):
        # self.filename=filename
        self.filename=open(filename,mode,encoding=encoding)
        self.mode=mode
        self.encoding=encoding

    def __getattr__(self, item):
        # print(item)
        return getattr(self.filename,item)
    def write(self,line):
        t=time.strftime('%Y-%m-%d %X')
        self.filename.write('%s %s'%(t,line))
    # def read(self):
    #     pass
    #
    # def write(self):
    #     pass

f1=Open('hehe.txt','w')
#触发getattr
# print(f1.read())
f1.write('11111111111111\n')
f1.write('2222222222222222\n')
f1.write('3333333333333\n')
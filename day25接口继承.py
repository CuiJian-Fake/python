import abc

class All_File(metaclass=abc.ABCMeta):#接口继承 一切皆文件

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass

class Disk(All_File):
    def read(self):
        print('Disk is read')

    def write(self):
        print('Disk is write')

class Cdrom(All_File):
    def read(self):
        print('Cdrom is read')

    def write(self):
        print('Cdrom is write')

class Mem(All_File):
    def read(self):
        print('Mem is read')

    def write(self):
        print('Mem is write')

m1=Mem()
print(Mem.__mro__)
m1.read()
m1.write()
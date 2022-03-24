class Vehicle:
    Country='china'

    def __init__(self,name,speed,load,power):
        self.name=name
        self.speed=speed
        self.load=load
        self.power=power

    def run(self):
        print('开动了')

class Subway(Vehicle):
    def __init__(self,name,speed,load,power,line):
        super().__init__(name,speed,load,power)#super 不加self
        self.line=line

    def show_info(self):
        print(self.name,self.line)

    def run(self):
        super().run()
        print('%s %s 线,开动啦'%(self.name,self.line))
line13=Subway('13号线','10km/s',100000,'电',13)

line13.show_info()
line13.run()
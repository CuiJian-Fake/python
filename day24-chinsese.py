

city='AA'
class chinese:#驼峰Chinese
    '我是中国人'
    dog='RB'
    city='BB'
    def __init__(self,name,sex,where):
        self.name = name
        self.sex = sex
        self.where = where
        print('-->',city)
    def tutan(self):
        print('%s正在吐痰' %self.name)
    def chadui(self):
        print('%s我要插队' % self.name)
    def chishi(self,food):
        print('%s正在吃%s' %(self.name,food))
p1 = chinese('SB','boy','TT')
print(p1.__dict__)
chinese.chadui(p1)
p1.chadui()#底层会自动传送p1
p1.tutan()#实例只有数据属性 没有函数属性 如果需要就跟类 要

p2 = chinese('ZZ','girl','RB')
p2.chishi('rice')

#函数定义名字动词加名词
#修改数据类型
print(chinese.dog)
chinese.dog='CN'
print(chinese.dog)
print(chinese.__dict__)

#增加数据类型

chinese.dang='共产党'
print(chinese.dang)
print(p1.dog)
print(p1.dang )

#删除

del chinese.dog,chinese.dang

# print(chinese.dang)
# print(p1.dog)
# print(p1.dang )

#给类增加一个函数属性
def eat_food(self,food):
    print('%sZZZZZZZZZZZZZZZZZZZZZZZ' %food)
chinese.eat=eat_food
p1.eat('zz')

#修改类的函数属性 覆盖它

#实例 增加数据属性
p1.age=18
print(p1.__dict__)

#给实例 增加函数属性

def test(self):
    print('我是来自实例的函数属性',self.name)

p1.test=test
print(p1.__dict__)
p1.test(p1)

#给实例删除一个属性

del p1.age
print(p1.__dict__)
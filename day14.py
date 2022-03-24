#!/usr/bin/env python
#coding:utf-8

#字符串
#数字
#列表
#元组
#字典

#可变不可变id号
#1.可变 列表 字典
#2.不可变 字符串 数字 元组

#访问顺序

#直接访问 数字
#1 顺序访问:字符串,列表，元组
#2 映射 字典

#存放元素个数
#容器类型:列表 元组 列表

#集合 不同元素组成 元素是无序的 集合中的元素 都是不可变类型
#s.discard('sb')删除元素不会报错
#s.remove('sb')会 报错

# python_1=['aaa','bbb','ccc']
# linux_1=['aaa','bbb']
# list=[]
# for p_name in python_1:
#     if p_name in linux_1:
#         list.append(p_name)
# print(list)

# pyhton_1=['lcg','szw','zjw','lcg']
# linux_1=['lcg','szw']
#
# p_s=set(pyhton_1)
# l_s=set(linux_1)
#
# print(p_s,l_s)
#
# print(p_s.intersection(l_s))#求交集
# print(p_s&l_s)
# print(p_s.union(l_s))#求并集
# print(p_s|l_s)
# print(p_s-l_s)#求差集
# print(p_s.difference(l_s))
# print(l_s.difference(p_s))
# print(p_s.symmetric_difference(l_s))#交叉补集
# print (p_s^l_s)
# p_s.difference_update(l_s)#p_s=p_s-l_s
# print(p_s)
#
# #集合是可变类型set frozenset不可变类型集合
#
# #字符串格式化
#
# print('i m %shobby is alex %s' % ('cj',1))
#
# t1 = "percent%.2f" % 99.1234567
# print(t1)
#
# tp1 = "i am %(name)s age %(age)d" % {'name':'alex','age':18}
# print(tp1)
#
# print('root','password',sep=':')

#format

#tp1 = 'i am {},age {},{}'.format("seven",18,"alex")
# tp1 = 'i am {0},age {1},{2}'.format("seven",18,"alex")
# print(tp1)
# tp1 = "i am {name} {age} {name}".format(**{'name':'alex','age':18})
# print(tp1)
# tp2="i am {:s} {:d}".format("alex",18)
# print(tp2)
# l=['sevev',18]
# tp3 = "i am {} {}".format(*l)
# print(tp3)
# v = [15,15,15,15,15,15.2837492,34]
# tp4 = "numbers : {:b},{:0},{:d},{:x},{:X},{:%},{}".format(*v)
# print(tp4)

#过程就是没有return返回值的函数

# def  test():
#     return 1
# print(test())

# def calc(x,y):
#     res = x**y
#     return res
# c = calc(11,2)
# print(c)
#
# def test(x,y,z):#位置参数
#     print(x)
#     print(y)
#     print(z)
#
# test(1,2,3)
# test(x=1,y=3,z=2)#位置无序固定
# test(1,4,z=2)#位置参数一定要关键字参数左边

# def handle(x,type='mysql'):
#     print(x)
#     print(type)
# handle('hello',type='sqlite')
# handle('hello','sqlite')
# handle('hello')
#
# def install(funcl=False,func2=True,func3=True):
#     pass

#**字典 *列表

#参数组

# def test(x,*args):
#     print(x)
#     print(args)
#     print(args[0])
#
# test(1,2,3,4,5,6)
# test(1,(2,3),[4,5])
#test([1,2,3,4])
# test(1,*[1,2,3,4,5])
# test(23,(123123,123123,1231231,))
# def test(x,**kwargs):
#     print(x)
#     print(kwargs)
# test(1,y=2,z=3)
# test(1,a=1,b=2)

def test(x,*args,**kwargs):
    'print'
    print(x)
    print(args)
    print(kwargs)

#test(x=1,y=2)
test(1,*[1,2,3],**{'a':1})


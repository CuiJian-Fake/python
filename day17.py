#!/usr/bin/env python
#coding:utf-8

# print(dict(zip(('a','b','c'),(1,2,3))))
# print(dict(zip({'a','b','c'},(1,2,3))))#zip 两个序列
#
# age_dic = {'age1':18,'age3':20,'age4':50,'age2':30}
# print(max(age_dic.values()))
#
# v = list(zip(age_dic.keys(),age_dic.values()))
#
# print(min(v))
# print(max(v))
# print(max(age_dic))
# L = ['a10','b12','c10',100]#不同类型间不能进行比较
# print(max(L))
L = ['a10','b2','c10']#不同类型间不能进行比较
# print(max(L))

people = [{'name':'alex','age':18},
          {'name':'aaa','age':50},
          {'name':'bb','age':30},
          {'name':'ccc','age':100},
        ]
# print(max(people,key=lambda x:x['age']))
#
#
# l = [1,2,3,4]
# print(list(reversed(l)))
#
# print(round(3.5))#四舍五入

# l = 'hello'
# s1 = slice(3,5)
# s2 = slice(1,4,2)
# print(l[3:5])
# print(l[s1])
# print(l[s2])
# print(s1.start,s1.stop,s1.step)

# a1 = [3,2,1,5,7]
# a2 = [3,2,'a',1,5,7]
# print(sorted(a1))
# print(sorted(a2))#排序本质就是在比较大小 同类型之间才可以比较

# print(sorted(people,key=lambda x:x['age']))
# name_dic = {'alex':200,
#             'wupeiqi':300,
#             'yuanhao':900,
#             }
# print(sorted(name_dic,key=lambda x:name_dic[x]))
#
# print(str('1'))
# print(type(str({'a':1})))
# dict_str = str({'a':1})
# print(type(eval(dict_str)))
#
# print(type(1))
#
# print(vars(int))#方法以字典的方式显示

# from test import si_hi as v
#
# v()

module = 'test'
m = __import__(module)
m.si_hi()
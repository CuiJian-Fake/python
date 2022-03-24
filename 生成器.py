#!/usr/bin/env python
#coding:utf-8

# def test():
#     yield  1
#     yield  2
#
# g=test()
# print(g)
# print(g.__next__())
# print(g.__next__())
#
# #三元表达式
# name='alex'
# #name='崔健'
# v='SB' if name=='alex' else '帅哥'
# print(v)
#
# #列表解析
# egg_list=[]
# for i in range(10):
#     egg_list.append("鸡蛋%s" % i)
# print(egg_list)
#
# l=[i for i in range(10)]
# print(l)
#
# ll=[i for i in range(10) if i > 5]
# print(ll)
#
# laomuji=('鸡蛋%s' %i for i in range(10))#生成器表达式
# print(laomuji)
# print(next(laomuji ))

# def product_baozi():
#     ret=[]
#     for i in range(100):
#         ret.append('包子%s' %i)
#     return  ret
# baozi_list=product_baozi()
# print(baozi_list)

def product_baozi():
    for i in range(100):
        yield ('包子%s' %i)

baozi_list=product_baozi()
print(baozi_list.__next__())



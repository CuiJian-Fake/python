#!/usr/bin/env python
#coding:utf-8

#print(abs(-1))

# v = []
# print(all(v))
#
# v1 = [1,2,3,4]
# print(all(v1))
#
# v2 = [1,2,3,'a']
# print(all(v2))
#
# v3 = [None]
# print(all(v3))
#
# v4 = [True]
# print(all(v4))
#
# v5 = ('A','C')
# print(all(v5))
#
# v6 = [0]
# print(all(v6))
#
# v7 = []
# print(all(v7))
#
# print(all(''))
#
# print(any(v7))

#print(bin(4))

# print(bytes('你好',encoding='UTF-8').decode('UTF-8'))
#
# ascii 不能编译中文
#
# print(chr(46))#数字ascii表
#
# print(divmod(10,3))#功能是用来分页的
#
# dic = {'name':'alex'}
# dict_str = str(dic)
# v = eval(dict_str)
# print(v)
#
# express = '1+2*(3/3-1)-2'
#
# print(eval(express))
#
# #可哈希的就是不可变的数据类型 不可hash的数据类型即可变数据类型
# print(hash('waefahgukarhga'))
# print(hash('udhfkgueafueufiaekguf'))
#
# dir()
# help()

print(bin(10))
print(hex(10))
print(oct(10))

print(isinstance([1,2],list))
print(isinstance({1,2,'a',(1,2)},set))

name = '哈哈哈哈嘿护法一'
print(globals())
print(__file__)
print(locals())

l = [1,3,100,-10,-1.1 ,0]
print(max(l))
print(min(l))




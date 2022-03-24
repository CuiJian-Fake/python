#!/usr/bin/env python
#coding:utf-8

l = [1,2,3,4,5]
# print(list(map(str,l)))

from functools import reduce

print(reduce(lambda x,y:x+y,l))


f=open('AAA','r+',encoding='utf-8')
f.write('ccdd')
f.close()

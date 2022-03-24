#!/usr/bin/env python
#coding:utf-8
# L = [1,2,3]
# # for i in L:
# #     print(i)
#
# L=L.__iter__()#for循环会有__iter__把对象变成可迭代对象之后__next__捕捉异常
#文件 字典 都可以
# print(L.__next__())
# print(L.__next__())
#
# x='hello'
# index=0
# while index<len(x):
#     print(x[index])
#     index+=1

l=[1,2,3,4,5]
l=l.__iter__()
while True:
    try:
        print(l.__next__())
    except StopIteration:
        print("迭代结束了")
        break
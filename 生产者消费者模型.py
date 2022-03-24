#!/usr/bin/env python
#coding:utf-8
import time

# def producter():
#     ret=[]
#     for i in range(10000):
#
#         ret.append('包子%s' %i)
#     return ret
#
# def consumer(res):
#     for index,baozi in enumerate(res):
#         time.sleep(0.1)
#         print('第%s个人,吃了%s' %(index,baozi))
#
# res=producter()
# consumer(res)

#yield相当于return 控制的是函数的返回值
def test():
    print('第一次')
    first=yield 1
    print('第二次',first)
    yield 2
    print('的第三次')
    yield 3
v=test()
print(v.__next__())
#v.__next__()
a=v.send('这就是ZZ')
print(a)
#!/usr/bin/env python
#coding:utf-8

# l=[1,3]
# l.__iter__()#iter(l)
#
# 装饰器:本质就是函数,功能是其他函数添加附加功能
#
# 原则:
# 1 不修改被修饰函数的原代码
# 2 不修改被修饰函数的调用方法

# import  time
# def cal(l):
#     start_time=time.time()
#     res=0
#     for i in l:
#         res+=i
#     stop_time=time.time()
#     print('函数的运行时间%s' %(stop_time-start_time))
#     return res
#
# print(cal(range(1000)))
#
# #装饰器的知识储备=高级函数+函数嵌套+闭包

# from decorate import timmer
import decorate
@decorate.timmer
def cal(l):

    res=0
    for i in l:
        res+=i

    return res

res=cal(range(10000))
print(res)
    

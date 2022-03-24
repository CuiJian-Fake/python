#!/usr/bin/env python
#coding:utf-8

# NAME = 'alex'
#
# def foo():
#     NAME = 'lihaifeng'
#     def bar():
#         print(NAME)
#     return bar
#
# foo()
#
#
# def test1():
#     print('in the test1')
# def test2():
#     print('in the test2')
#     return test1
#
# res = test2()
# print(res())
# print(test2()())
#
# name = 'alex'
#
# def foo():
#     name = '1hf1'
#     def bar():
#         name = 'cj'
#         def tt():
#             print(name)
#         return tt
#     return bar
# print(foo)
# v = foo()
# v()()

#匿名函数 lambda x:x+1


def calc(x):
    return x+1

print(calc(10))

print(lambda x:x+1)

func = lambda a,b:a+b
print(func(1,2))

name = 'alex'
v = lambda x:x+'_sb'
print(v(name))

name1 = 'alex'
name2 = 'sbalex'
name3 = 'superalex'

v = lambda x,y,z:(x+1,y+1,z+1)
print(v(1,2,3))

#编程的方法论
#面向对象
#面向过程 模拟解决问题的流程
#函数式 编程语言定义的函数+数学意义的函数

#尾递归 最一步调用递归




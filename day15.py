#!/usr/bin/env python
#coding:utf-8
#全局变量 局部变量

#全局变量
# name = 'alex'
# def test():
#     # global name
#     name = 'cj'
#     print(name)#cj
# test()
# print(name)

# name = '刚娘'

# def weihou():
#     name = '陈卓'
#     def weiweihou():
#         global  name
#         name = '冷静'
#     weiweihou()
#     print(name)
#
# print(name)
# weihou()
# print(name)
# 刚娘
# 陈卓
# 冷静

#有局部变量的 先局部变量

# def weihou():
#     name = '陈卓'
#     def weiweihou():
#         nonlocal  name#指定上级变量
#         name = '冷静'
#         print(name)
#     weiweihou()
#     # print(name)
#
# print(name)
# weihou()
# print(name)




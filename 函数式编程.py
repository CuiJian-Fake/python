#!/usr/bin/env python
#coding:utf-8

#高阶函数 1把函数当做参数传给另外一个函数 2返回值包含函数
# def foo(n):
#     print(n)
#
# def bar(name):
#     print('my name is %s' % name)
#
# foo(bar('alex'))

#返回值可以是任何值得函数包括自己
def foo():
    print('from foo')
    return foo

print(foo())

def test1():
    print('from test')

def test2():
    print('from test2')
    return test1()

test2()
#!/usr/bin/env python
#coding:utf-8

#风湿理论：函数即变量

def bar():
    print('from bar')

def foo():
    print('from foo')
    bar()

# def bar():
#     print('from bar')

foo()
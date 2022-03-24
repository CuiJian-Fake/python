#!/usr/bin/env python
#coding:utf-8

# 高级函数的定义
# 1函数的接收的参数是一个函数名
# 2函数的返回值是一个函数名
# 3满足上面2个任意一个，都可以称之为高级函数

import time
def foo():
    time.sleep(3)
    print('你好林师傅')

def timmer(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('运行时间%s' % (start_time-stop_time))
    return func

foo=timmer(foo)
foo()


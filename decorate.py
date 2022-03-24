#!/usr/bin/env python
#coding:utf-8
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('函数的运行时间%s' % (stop_time - start_time))
        return res
    return wrapper

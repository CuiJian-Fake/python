#!/usr/bin/env python
#coding:utf-8
import time
def timmer(func):
    def warpper():
        print(func)
        func()
        pass
    return warpper
@timmer  #test=timmer(test)
def test():
    time.sleep(3)
    print('test函数运行完毕')
test()


l=[1,2,3,5,6,7,8]
a,b,*_,c,d=l
print(a,b,c,d)
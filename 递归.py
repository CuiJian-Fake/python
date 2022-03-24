#!/usr/bin/env python
#coding:utf-8

#递归
#必须有一个明确的结束条件
#没执行一次递归数都在减小
#效率不高

import time

def calc(n):
    #print(n)
    # time.sleep(10)

    if int(n/2) == 0:
        return  n
    res = calc(int(n/2))
    return res

v = calc(10)
print(v)
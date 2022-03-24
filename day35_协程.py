'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/30/2020 4:58 PM
@Software: PyCharm
@File    : day35_协程.py
'''

#协程 协作式--------非抢占式的程序
# yeild()协程的关键词
#用户态的切换
#关键点是什么时候切换
#greenlet切换     switch切换
#协程主要是解决IO操作
#协程本质就是一个线程
#协程的优势： 没有切换的消耗 没有锁的概念 不能用多核 所以协程+进程 并发


# from greenlet import greenlet
#
# def test1():
#     print(1)
#     gr2.switch()
#     print(2)
#     gr2.switch()
#
# def test2():
#     print(3)
#     gr1.switch()
#     print(4)
#
# gr1=greenlet(test1)
# gr2=greenlet(test2)
#
# gr1.switch()

import gevent
import requests,time


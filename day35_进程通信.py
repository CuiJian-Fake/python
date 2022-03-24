'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/30/2020 2:38 PM
@Software: PyCharm
@File    : day35_进程通信.py
'''

import queue,time
import multiprocessing

def  foo(q):
    time.sleep(1)
    q.put(123)
    q.put('cj')


if __name__ == '__main__':
    q=multiprocessing.Queue()

    p=multiprocessing.Process(target=foo,args=(q,))

    p.start()

    print(q.get())
    print(q.get())


#通过管道 Pipe




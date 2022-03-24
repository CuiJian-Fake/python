'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/25/2020 3:15 PM
@Software: PyCharm
@File    : day34_同步锁.py
'''

import threading
import  time

num=100

def sub():
    global num
    lock.acquire()
    gun=num
    time.sleep(0.001)
    num=gun-1
    lock.release()

l=[]

lock=threading.Lock()
for i in range(0,100):
    t=threading.Thread(target=sub)
    t.start()
    l.append(t)

for i in l:
    i.join()

print(num)
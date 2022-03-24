'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/23/2020 5:10 PM
@Software: PyCharm
@File    : day33_threading_lesson.py
'''

import threading
import time

def music():
    print("begin to listen %s" %time.ctime())
    time.sleep(3)
    print("stop to listen %s" %time.ctime())

def game():
    print("begin to play game %s" %time.ctime())
    time.sleep(5)
    print("stop to play game %s" %time.ctime())

t1=threading.Thread(target=music)
t2=threading.Thread(target=game)
threads=[]
threads.append(t1)
threads.append(t2)
if __name__ == '__main__':
    #t2.setDaemon(True)
    for t in threads:
        t.start()
        t.join()
       # print(threading.active_count())#活跃的线程目前
    while threading.active_count()==1:
     print("end================================")
     break

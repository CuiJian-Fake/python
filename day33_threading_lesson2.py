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

if __name__ == '__main__':
    # t1=threading.Thread(target=music)
    # t1.start()
    #
    # t2=threading.Thread(target=game)
    # t2.start()
    #
    # t1.join()
    # t2.join()
    #
    # print("ending......")

    t1=threading.Thread(target=music)
    t2=threading.Thread(target=game)
    l=[]
    l.append(t1)
    l.append(t2)

    for t in l:
        t.start()
        t.join()
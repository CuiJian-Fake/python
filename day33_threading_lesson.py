'''
-*- coding: utf-8 -*-
@Author  : CJ
@Time    : 11/23/2020 5:10 PM
@Software: PyCharm
@File    : day33_threading_lesson.py
'''

import threading
import time

def Hi(num):
    print("hello %d" %num)
    time.sleep(3)

if __name__ == '__main__':
    t1=threading.Thread(target=Hi,args=(9,))
    t1.start()

    t2=threading.Thread(target=Hi, args=(10,))
    t2.start()

    print("\nending......")
